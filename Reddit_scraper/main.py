import pymongo
from pymongo import MongoClient
import pymysql.cursors
from destroy_tables import *
from build_sqldb import *
from convert_json_to_sql import *
from build_mongo import *
import os
connection = pymysql.connect(host='lolsql.stat.ncsu.edu', user='LOLwrite',password='LaberLabsLOLwrite',db='lol_test',charset='utf8mb4')
# connection = pymysql.connect(host='localhost',
# 	                             user='root',
# 	                             password='dongs420',
# 	                             db='LeagueDB',
# 	                             charset='utf8mb4',
# 	                             cursorclass=pymysql.cursors.DictCursor)


os.system("pip install -r requirements.txt")

print "Cleaning MYSQLDB"
#destroy(connection)
print "Building MYSQL DB"
#build(connection)
print "Building MONGO DB"
#build_db()
print "Filling DB"

#build_db_items(connection)

try:
	build_db_champions(connection)
except:
	pass
try:
	build_db_reddit(connection)
except:
	pass
connection.close()
print "Done"
