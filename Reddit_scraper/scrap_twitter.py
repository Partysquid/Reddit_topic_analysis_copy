from consume_data_sql import *
import pymysql


connection = pymysql.connect(host='***', user='***',password='***',db='***',charset='utf8mb4')
x=consume(connection)
x.run_prog()
