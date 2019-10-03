import pymysql
import pymysql.cursors
import time

#Create a connection objection to connect to lol_test, where RedditThreads and RedditComments Tables are located 

connection = pymysql.connect(host='lolsql.stat.ncsu.edu', user='LOLread',password='LaberLabsLOLquery',db='lol_test',charset='utf8mb4')

print(connection)



with connection.cursor() as cursor:
	#get all information of the 20th thread put into the DB
	sql = "SELECT * from RedditThreads WHERE `id`=20"
	cursor.execute(sql)
	result= cursor.fetchone()
	print(result)

	#get the body i.e comment text of each comment for thread 20 in DB
	sql = "SELECT `body` from RedditComments WHERE `id`=20"
	cursor.execute(sql)
	comments= cursor.fetchall()
	print("We have "  + str(len(comments)) + "total titles")
	time.sleep(.5)
	#print them out slowly
	for comment in comments:
		time.sleep(.5)
		print("Comment:")
		#we only asked for some thing back, so we have a singleton tuple, so the information is in the 0 element of the tuple
		print(str(comment[0]))


	#you can build more complex SQL statements, including variables, etc. Go here to see https://pymysql.readthedocs.io/en/latest/user/examples.html

# mysql -u LOLwrite -h lolsql.stat.ncsu.edu -p
# Enter password: 
# Welcome to the MySQL monitor.  Commands end with ; or \g.
# Your MySQL connection id is 346155
# Server version: 5.5.5-10.3.7-MariaDB-log mariadb.org binary distribution

# Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

# Oracle is a registered trademark of Oracle Corporation and/or its
# affiliates. Other names may be trademarks of their respective
# owners.
