import praw
import pandas as pd
import datetime as dt

#Program parameters#####
new_reddit_data = pd.DataFrame.from_csv("new_reddit_data.csv")
reddit = praw.Reddit(client_id='N', \
                     client_secret='', \
                     user_agent='League Scraper', \
                     username='', \
                     password='')

subreddit = reddit.subreddit('LeagueofLegends')

### Script #########
while True:
    new_subreddit = subreddit.new(limit=100)

    for submission in subreddit.new(limit=1):
        print(submission.title, submission.id)
    
    topics_dict = { "title":[],
                   "score":[],
                   "id":[], "url":[], 
                   "comms_num": [],
                   "created": [],
                   "body":[]}

    for submission in new_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)
    

    topics_data = pd.DataFrame(topics_dict)

    def get_date(created):
        return dt.datetime.fromtimestamp(created)
    _timestamp = topics_data["created"].apply(get_date)
    topics_data = topics_data.assign(timestamp = _timestamp)

    newest_old_data = new_reddit_data.head(200)

    combined_data = pd.concat([newest_old_data, topics_data, newest_old_data])
    combined_data = combined_data.drop_duplicates(subset="id", keep=False)

    new_reddit_data = pd.concat([new_reddit_data, combined_data])
    new_reddit_data.to_csv("new_reddit_data.csv")


### Currently In Progress######
