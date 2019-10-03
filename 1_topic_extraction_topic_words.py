import pandas as pd
import numpy as np
import json
import random
import Helper_Functions as hf
import time
import string
from collections import defaultdict
from collections import Counter
#%%
#DATA

reddit_assigned_topics = pd.read_csv("assigned_reddit_topics.csv", index_col = 0)
normalized_term_matrix = pd.read_csv("normalized_term_matrix.csv", index_col = 0)

#seperate df into lists based on topic
topic_0 = reddit_assigned_topics['Text'][reddit_assigned_topics['assigned_topic']==0].values
topic_1 = reddit_assigned_topics['Text'][reddit_assigned_topics['assigned_topic']==1].values
topic_2 = reddit_assigned_topics['Text'][reddit_assigned_topics['assigned_topic']==2].values
topic_3 = reddit_assigned_topics['Text'][reddit_assigned_topics['assigned_topic']==3].values
topic_4 = reddit_assigned_topics['Text'][reddit_assigned_topics['assigned_topic']==4].values

topics = [topic_0, topic_1, topic_2, topic_3, topic_4]

#%%
#Functions
#counts each word used in ALL of the documents, stores in dataframe
def count_words(reddit_assigned_topics, i):
    results = Counter()
    
    reddit_assigned_topics['Text'][reddit_assigned_topics['assigned_topic']==i].str.replace('[{}]'.format(string.punctuation), ' ').str.lower().str.split().apply(results.update)


    return(results)        
    

#%%
#Main

word_counts = [0,0,0,0,0]

for i in range (5):
    word_counts[i] = count_words(reddit_assigned_topics, i)
    
word_count_df_0 = pd.DataFrame.from_dict(word_counts[0], orient='index').reset_index()
word_count_df_0 = word_count_df_0.rename(index=str, columns={"index": "Word", 0: "count_0"})

word_count_df_1 = pd.DataFrame.from_dict(word_counts[1], orient='index').reset_index()
word_count_df_1 = word_count_df_1.rename(index=str, columns={"index": "Word", 0: "count_1"})

word_count_df_2 = pd.DataFrame.from_dict(word_counts[2], orient='index').reset_index()
word_count_df_2 = word_count_df_2.rename(index=str, columns={"index": "Word", 0: "count_2"})

word_count_df_3 = pd.DataFrame.from_dict(word_counts[3], orient='index').reset_index()
word_count_df_3 = word_count_df_3.rename(index=str, columns={"index": "Word", 0: "count_3"})

word_count_df_4 = pd.DataFrame.from_dict(word_counts[4], orient='index').reset_index()
word_count_df_4 = word_count_df_4.rename(index=str, columns={"index": "Word", 0: "count_4"})

word_df_list = [word_count_df_1,word_count_df_2,word_count_df_3,word_count_df_4]

total_word_counts = word_count_df_0
for x in word_df_list:
    total_word_counts = total_word_counts.merge(x, how = 'inner', on = ['Word'])
    
total_word_counts["total_count"] = total_word_counts["count_0"] + total_word_counts["count_1"] + total_word_counts["count_2"] + total_word_counts["count_3"] + total_word_counts["count_4"]


total_word_counts["P(T|W)_0"] = total_word_counts["count_0"]/total_word_counts["total_count"]
total_word_counts["P(T|W)_1"] = total_word_counts["count_1"]/total_word_counts["total_count"]
total_word_counts["P(T|W)_2"] = total_word_counts["count_2"]/total_word_counts["total_count"]
total_word_counts["P(T|W)_3"] = total_word_counts["count_3"]/total_word_counts["total_count"]
total_word_counts["P(T|W)_4"] = total_word_counts["count_4"]/total_word_counts["total_count"]
#word_counts = count_words(reddit_assigned_topics)
#
#word_count_df = pd.DataFrame.from_dict(word_counts, orient='index').reset_index()
#word_count_df = word_count_df.rename(index=str, columns={"index": "Word", 0: "count"})
#
#total_count = word_count_df["count"].sum()
#
#word_count_df["probability"] = word_count_df["count"]/total_count
#
#merged_df = normalized_term_matrix.merge(word_count_df, how = 'inner', on = ['Word'])
#
#for i in range(5):
#    merged_df[str(i) + "_P(T | W )"] = merged_df[str(i)]/merged_df["probability"]
#


#what needs to be done:
    
    #go back and refine the filter, remember to replace k\da with "kdareplacement"
    #compare the terms to the actual topics
