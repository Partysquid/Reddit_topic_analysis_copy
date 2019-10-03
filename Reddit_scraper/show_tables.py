import pymongo
from pymongo import MongoClient
import pymysql.cursors

connection = pymysql.connect(host='lolsql.stat.ncsu.edu', user='LOLwrite',password='LaberLabsLOLwrite',db='lol',charset='utf8mb4')

with connection.cursor() as cursor:
	#sql = "show tables"
	sql = "select * from ItemsTwitter"
	cursor.execute(sql)
	tables = cursor.fetchall() 
	print tables
