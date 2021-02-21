from consume_reddit_sql import *


reddit_data_dict = { "title":[],
                "score":[],
                "id":[], "url":[], 
                "comms_num": [],
                "created": [], 
                "body":[]}

x=consume_reddit(reddit_data_dict)
x.startBot()
