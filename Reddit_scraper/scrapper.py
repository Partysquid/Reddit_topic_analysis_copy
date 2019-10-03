from consume_reddit_sql import *
# connection = pymysql.connect(host='localhost',
# 	                             user='root',
# 	                             password='dongs420',
# 	                             db='LeagueDB',
# 	                             charset='utf8mb4',
# 	                             cursorclass=pymysql.cursors.DictCursor)


#old code for database auto upload
#connection = pymysql.connect(host='lolsql.stat.ncsu.edu', user='LOLwrite',password='LaberLabsLOLwrite',db='lol_test',charset='utf8mb4')
#x=consume_reddit(connection)

reddit_data_dict = { "title":[],
                "score":[],
                "id":[], "url":[], 
                "comms_num": [],
                "created": [], 
                "body":[]}

x=consume_reddit(reddit_data_dict)
x.startBot()