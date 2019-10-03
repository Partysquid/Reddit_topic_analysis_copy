from consume_data_sql import *
import pymysql
# connection = pymysql.connect(host='localhost',
# 	                             user='root',
# 	                             password='dongs420',
# 	                             db='LeagueDB',
# 	                             charset='utf8mb4',
# 	                             cursorclass=pymysql.cursors.DictCursor)

connection = pymysql.connect(host='lolsql.stat.ncsu.edu', user='LOLwrite',password='LaberLabsLOLwrite',db='lol_test',charset='utf8mb4')
x=consume(connection)
x.run_prog()