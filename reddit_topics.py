from __future__ import print_function
from time import time

import Helper_Functions as HF
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
import pandas as pd
import numpy as np
import re
from numpy import NaN
from random import shuffle


## Program parameters ##############

n_features = 1500 #number of words counted to create LDA predictions
n_components = 5 #number of topics
n_top_words = 15 #number of words that build a topic
max_df_num = .80 #percent of documents it needs to be less than to be considered a topic word
min_df_num = 2#min number of documents it needs to be in to be considered topic word
top_topics = []
stop_words_file = open("stopwordslist.txt", "r")
stop_words_list = stop_words_file.read().split(',')
champion_names_file = open("champions.txt", "r")
champions_list = champion_names_file.read().split('\n')
nicknames_file = open("nicknames.txt", "r")
nicknames_list = nicknames_file.read().split('\n')
champions_list = champions_list + nicknames_list
replace_champ_string = " replacementchampionstring "
#%%
####-Functions-###########################
def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        #top_topics = top_topics.append(topic_idx)
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()
    
# def replace_champion_names(string):
#    
#    for champ_name in champions_list:
#        myRe = re.compile('[\s^]' + champ_name + '\'s\s', re.IGNORECASE)
#        string = myRe.sub(replace_champ_string, string)
#        myRe = re.compile('[\s^]' + champ_name + '\s', re.IGNORECASE)
#        string = myRe.sub(replace_champ_string, string)
#        myRe = re.compile('[\s^]' + champ_name + '*[,.\'"`:-\?!/]', re.IGNORECASE)
#        string = myRe.sub(replace_champ_string, string)
#    return(string)

def create_champion_compiles():
    compiled_list = list(np.zeros(3*len(champions_list)))
    i = 0
    for champ_name in champions_list:
        myRe = re.compile(champ_name + '\'s\s', re.IGNORECASE)
        compiled_list[i] = myRe
        i = i + 1
        myRe = re.compile(champ_name + '\s', re.IGNORECASE)
        compiled_list[i] = myRe
        i = i + 1
        myRe = re.compile(champ_name + '[,.\'"`:-\?!/ ]', re.IGNORECASE)
        compiled_list[i] = myRe
        i = i + 1
    return(compiled_list)
    

def optimized_replace_champion_names(string):
    myRe = re.compile("k/da" + '[,.\'"`:-\?!/ ]', re.IGNORECASE)
    newstring = myRe.sub(' kdareplacement ', string)
    for regex_sub in compiled_list:
        newstring = regex_sub.sub(replace_champ_string, newstring)
    return(newstring)
    
def topic_sort(row):
    x = row[['Topic 0', 'Topic 1', 'Topic 2', 'Topic 3', 'Topic 4']].max()
    return{
            row['Topic 0']: 0,
            row['Topic 1']: 1,
            row['Topic 2']: 2,
            row['Topic 3']: 3,
            row['Topic 4']: 4
            }.get(x, NaN)
#%%
###############################################################################
    #Data Processing#
print("Loading dataset...")
t0 = time()  
if(False):
#if (HF.check_file("final_formatted_reddit_df.csv")):
    reddit_df =pd.read_csv("final_formatted_reddit_df.csv")
else:
    reddit_df = pd.read_csv("Reddit_Text_AND_Bodies.csv")

    print("done in %0.3fs." % (time() - t0))
    print("Clearing empty values in dataset...")
    t0 = time() 
    reddit_df = reddit_df.dropna()
    
    print("done in %0.3fs." % (time() - t0))
    
    print("Joining columns in dataset...")
    t0 = time()
    
    
    reddit_df['Text'] = reddit_df['Title'] + ' ' + reddit_df['Body_Text']
    
   
    
    print("done in %0.3fs." % (time() - t0))
    
    
    print("Removing champion names in data...")
    t0 = time()
    
    compiled_list = create_champion_compiles()
    reddit_df['Formatted_Text'] = reddit_df['Text'].apply(optimized_replace_champion_names)
    
    reddit_df.to_csv("final_formatted_reddit_df.csv")
print("done in %0.3fs." % (time() - t0))


print("Converting data into list...")
t0 = time()
n_samples = len(reddit_df) #         number of threads to run LDA on


reddit_list = list(reddit_df['Formatted_Text'].values)

data_samples = reddit_list[:n_samples]
test_data_samples = data_samples.copy()

print("done in %0.3fs." % (time() - t0))

###############################################################################
#%%

# Use tf-idf features for NMF.
print("Extracting tf-idf features for NMF...")
tfidf_vectorizer = TfidfVectorizer(max_df=max_df_num, min_df=min_df_num,
                                   max_features=n_features,
                                   stop_words=stop_words_list)
t0 = time()
tfidf = tfidf_vectorizer.fit_transform(data_samples)
print("done in %0.3fs." % (time() - t0))

# Use tf (raw term count) features for LDA.
print("Extracting tf features for LDA...")
tf_vectorizer = CountVectorizer(max_df=max_df_num, min_df=min_df_num,
                                max_features=n_features,
                                stop_words=stop_words_list)
t0 = time()
tf = tf_vectorizer.fit_transform(data_samples)
print("done in %0.3fs." % (time() - t0))
print()



print("Fitting LDA models with tf features, "
      "n_samples=%d and n_features=%d..."
      % (n_samples, n_features))
lda = LatentDirichletAllocation(n_components=n_components, max_iter=5,
                                learning_method='batch',
                                learning_offset=50.,
                                random_state=0)
t0 = time()
lda.fit(tf)
print("done in %0.3fs." % (time() - t0))

print("\nTopics in LDA model:")
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words )

#%%
    #running tests#
test_set_vectorized = tf_vectorizer.fit_transform(test_data_samples)
predict = lda.transform(test_set_vectorized)

prediction_df = pd.DataFrame({'Text':test_data_samples})
for i in range(5):
    prediction_df['Topic ' + str(i)] = predict[:,i]
#%%
topic = 0
topics_heads = pd.DataFrame()
for topic in range(n_components):
    topic_head = prediction_df.sort_values(by = ('Topic ' + str(topic)), ascending = False).head(20)
    topics_heads = topics_heads.append(topic_head)


topics_heads.to_csv("topics_heads.csv")

#features_vect = tf_vectorizer.fit_transform(tf_feature_names)


#%%
prediction_df['assigned_topic'] = prediction_df.apply(lambda row: topic_sort(row), axis=1)

sorted_reddit_df = prediction_df.drop(['Topic 0', 'Topic 1', 'Topic 2', 'Topic 3', 'Topic 4'], axis=1)

sorted_reddit_df.to_csv("assigned_reddit_topics.csv")
#%%
#components_of_words = lda.components_
normalization = lda.components_ / lda.components_.sum(axis=1)[:, np.newaxis]

norm_df = pd.DataFrame(normalization.T)

norm_df['Word'] = tf_feature_names

norm_df.to_csv("normalized_term_matrix.csv")

#notes

# seperate data cleaning into different script
# load cleaned data each time run this one



#use tf idf to find the topic words for each 
#   make sure you create a 2 wide list of the reddit posts and their assigned topics
#  can use sklearn for tfidf
