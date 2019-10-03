from consume_reddit_sql import *

connection = pymysql.connect(host='lolsql.stat.ncsu.edu', user='LOLwrite',password='LaberLabsLOLwrite',db='lol_test',charset='utf8mb4')

command = "ALTER TABLE `redditcomments` CHANGE COLUMN `post_dt` `post_dt` datetime DEFAULT CURRENT_TIMESTAMP"
command2 = "ALTER TABLE `redditthreads` CHANGE COLUMN `post_dt` `post_dt` datetime DEFAULT CURRENT_TIMESTAMP"
#command1 = "ALTER TABLE `redditcomments` CHANGE COLUMN `ups` `voting_score` INT"
#command2 = "ALTER TABLE `redditcomments` DROP COLUMN `downs`"
#command = "ALTER TABLE `redditthreads` DROP COLUMN `downs`"
with connection.cursor() as cursor:
	cursor.execute(command)
	connection.commit()
	cursor.execute(command2)
	connection.commit()