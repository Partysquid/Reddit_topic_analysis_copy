import praw
import time
from pymongo import MongoClient
import pymysql.cursors
from destroy_tables import *
from build_sqldb import *
from convert_json_to_sql import *
from build_mongo import *
class consume_reddit:
	def __init__(self,connection):
		try:
			self.reddit = praw.Reddit(client_id='ID',
	                     client_secret='CLIENTSECRET',
	                     password='PW',
	                     user_agent='Getting League info from league subreddits',
	                     username='REDDITNAME')
			self.sublist=["leagueoflegends","LoLeventVoDs","summonerschool"]
			self.other = ['SwainMains', 'JhinMains', 'JarvanIVMains', 'RenektonMains', 'DrMundoMains', 'EzrealMains', 'IreliaMains', 'MalphiteMains', 'Illaoi', 'MorganaMains', 'GalioMains', 'SyndraMains', 'EvelynnMains', 'GragasMains', 'ViktorMains', 'WukongMains', 'XayahMains', 'KennenMains', 'LissandraMains', 'Sivir', 'BardMains', ' CaitlynMains', 'VladimirMains', 'VolibearMains', 'UrgotMains', 'RekSaiMains', 'LeeSinMains', 'VarusMains', 'TheSecretWeapon', 'LeagueofJinx', 'LucianMains', 'ThreshMains', 'TwitchMains', 'TeemoTalk', 'MordekaiserMains', 'RivenMains', 'XerathMains', 'Lux', 'OriannaMains', 'DianaMains', 'ZoeMains', 'HeimerdingerMains', 'YorickMains', 'TristanaMains', 'RumbleMains', 'DirtySionMains', 'ZileanMains', 'Kindred', 'VeigarMains', 'CassiopeiaMains', 'SonaMains', 'GarenMains', 'GnarMains', 'TwistedFateMains', 'GravesMains', 'Aurelion_Sol_Mains', 'ShyvanaMains', 'NocturneMains', 'ZyraMains', 'MissFortuneMains', 'LeonaMains', 'RengarMains', 'AzirMains', 'Shen', 'TaliyahMains', 'FiddlesticksMains', 'HecarimMains', 'JayceMains', 'KatarinaMains', 'FioraMains', 'KalistaMains', 'RyzeMains', 'AsheMains', 'EkkoMains', 'ChoGathMains', 'Kog_Mains', 'MasterYiMains', 'UdyrMains', 'ornnmains', 'PantheonMains', 'TrundleMains', 'OlafMains', 'RakanMains', 'NidaleeMains', 'SorakaMains', 'KarmaMains', 'KassadinMains', 'YasuoMains', 'QuinnMains', 'CamilleMains', 'TaricMains', 'RammusMains', 'Velkoz', 'KaisaMains', 'KayleMains', 'JaxMains', 'AniviaMains', 'BlitzcrankMains', 'MalzaharMains', 'WarwickMains', 'ShacoMains', 'GangplankMains', 'AkaliMains', 'Alistar', 'SkarnerMains', 'LuluMains', 'AhriMains', 'NasusMains', 'DariusMains', 'IvernMains', 'AmumuMains', 'Draven', 'TahmKenchMains', 'ViMains', 'SejuaniMains', 'BrandMains', 'AatroxMains', 'NamiMains', 'VayneMains', 'CorkiMains', 'TalonMains', 'MaokaiMains', 'ZiggsMains', 'NunuMains', 'KhaZixMains', 'SingedMains', 'EliseMains', 'LeblancMains', 'XinZhaoMains', 'FizzMains', 'Janna', 'KarthusMains', 'BraumMains', 'ZedMains', 'PoppyMains', 'KaynMains', 'TryndamereMains', 'NautilusMains']
			self.sublist=self.sublist+self.other
			print("starting Bot")
			self.connection = connection
		except Exception as e:
				print(e)
			



	def startBot(self):
		counter=0
		my=0
		notdone=True
		cursor_counter=None	
		connection = self.connection
		with connection.cursor() as cursor:
			while notdone:
				print("Moving on")
				try:
					for i in range(0,len(self.sublist)):
						x=self.sublist[i]
						try:
							submissions = self.reddit.subreddit(x).hot(limit=200)
						except Exception as e:
							print(e)
							print("died")
						for submission in submissions:
							#comment 'created', 'created_utc',
							try:

								sql = "SELECT MAX(id) from RedditThreads"
								cursor.execute(sql)
								result= cursor.fetchone()

								if(result[0] is None):
									cursor_counter =1
								else:
									cursor_counter = result[0] +1
								print("counter")
								print(cursor_counter)
								commentdicList=[]
								entry={}
								print(submission.created)
								print(submission.created_utc)
								entry["id"] = submission.id
								entry["title"] = submission.title.encode('ascii', 'ignore')
								entry["ups"] = submission.ups
								entry["downs"] = submission.downs
								entry["url"] = submission.url
								entry["viewcount"] = submission.view_count
								print(submission.view_count)
								entry["name"] = submission.name.encode('ascii', 'ignore')
								entry["text"]=submission.selftext.encode('ascii', 'ignore')
								entry["created"]=submission.created
								entry["created_utc"] = submission.created_utc
								entry["permalink"]=submission.permalink	
								cursor.execute("""SELECT * FROM RedditThreads WHERE Title=%s""",(entry['title'],))
								result= cursor.fetchone()
								db_id = None
								#time.sleep(10)
								print("result")
								print(result)
								if result is not None:
									db_id = result[0]
									subreddit = self.sublist[i]
									reddit_id=entry["id"] 
									title=entry["title"]
									ups = int(entry["ups"]) 
									downs= int(entry["downs"]) 
									if(ups>=0):
										pass
									else:
										ups =downs
									url= entry["url"]
									viewcount= entry["viewcount"] 
									name =  entry["name"]
									text = entry["text"]
									created = entry["created"]
									created_utc = entry["created_utc"]
									permalink = entry["permalink"]
									cursor.execute("""UPDATE RedditThreads SET subreddit=%s,reddit_id=%s,Title=%s, Body_Text=%s, voting_score=%s, url=%s,viewcount=%s,user_name=%s, created=%s, created_utc=%s, permalink=%s WHERE id=%s""",(str(subreddit),str(reddit_id),str(title),str(text),str(ups),str(url),str(viewcount),str(name),str(created),str(created_utc),str(permalink),str(db_id)))
									connection.commit()
								else:
									db_id = cursor_counter
									subreddit = self.sublist[i]
									reddit_id=entry["id"] 
									title=entry["title"]
									ups = int(entry["ups"]) 
									downs= int(entry["downs"]) 
									url= entry["url"]
									viewcount= entry["viewcount"] 
									name =  entry["name"]
									text = entry["text"]
									created = entry["created"]
									created_utc = entry["created_utc"]
									permalink = entry["permalink"]
									if(ups>=0):
										pass
									else:
										ups =-downs
									
									sql = "INSERT INTO `RedditThreads` (`subreddit`,`reddit_id`,`Title` , `Body_Text`, `voting_score`,  `url`,`viewcount`,`user_name` , `created` , `created_utc` , `permalink`)  VALUES (%s,%s, %s,%s, %s,%s, %s,%s,%s,%s,%s)"
									cursor.execute(sql, (str(subreddit),str(reddit_id),str(title),str(text),str(ups),str(url),str(viewcount),str(name),str(created),str(created_utc),str(permalink)))
									connection.commit()

								print("Done with" +str(title))
								submission.comments.replace_more(limit=None)
									
								for comment in submission.comments.list():
									try:
										temp_comment_dir={}
										temp_comment_dir["name"] = comment.name.encode('ascii', 'ignore')
										temp_comment_dir["ups"] = comment.ups
										temp_comment_dir["downs"] = comment.downs
										temp_comment_dir["id"] = comment.id
										temp_comment_dir["text"] = comment.body.encode('ascii', 'ignore')
										temp_comment_dir["created"]=comment.created
										temp_comment_dir["created_utc"] = comment.created_utc
										name= temp_comment_dir["name"]
										ups = temp_comment_dir["ups"]
										downs = temp_comment_dir["downs"]
										id_red = temp_comment_dir["id"]
										text= temp_comment_dir["text"]
										cursor.execute("""SELECT * FROM RedditComments WHERE reddit_id=%s""",(id_red,))
										if(ups>=0):
											pass
										else:
											ups =-downs


										result= cursor.fetchone()
										print(result)
										if result is not None:
											cursor.execute("""UPDATE RedditComments SET id=%s, user_name=%s, reddit_id=%s, voting_score=%s, body=%s, created=%s, created_utc=%s WHERE reddit_id =%s""", (str(db_id),str(name),str(id_red),str(ups),str(text),str(id_red),str(created),str(created_utc)))
											print("UPDATED comment")
											connection.commit()
										else:

											sql = "INSERT INTO `RedditComments` (`id`, `user_name`, `reddit_id`, `voting_score`, `body`,`created`,`created_utc`)  VALUES (%s,%s, %s,%s, %s,%s,%s)"
											
											cursor.execute(sql, (str(db_id),str(name),str(id_red),str(ups),str(text),str(created),str(created_utc)))
											print("new comment entry " + str(id_red))
											connection.commit()
										#print("Posted Comment " + str(text))
									except Exception as e :
										print("bug1")
								print("Made new entry for " + str(entry["title"]))
							except Exception as e:
								print(e)
								print("bug4")
								continue
					print("Taking a Nap")
					time.sleep(3600)
				except Exception as e:
					print(e)
					print("bug5")
					continue









