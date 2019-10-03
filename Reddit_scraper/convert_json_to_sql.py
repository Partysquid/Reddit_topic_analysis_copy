import pymongo
from pymongo import MongoClient
import pymysql.cursors

def build_db_champions(connection):
	client = MongoClient('localhost')
	db = client['LeagueDB']
	collection1=db['Champions']

	counter=0
	print("starting")
	for entry in collection1.find():
		dic = entry
		name = dic["name"]
		tweet_list = dic["tweet_list"]

		for tweet in tweet_list:
			try:
				with connection.cursor() as cursor:
					sql = "INSERT INTO `ChampionsTwitter` (`Champion_Name`, `Tweet_Text`,`Coor`,`Geo`,`Created_At`,`Sent_Pol`,`Sent_Sub`,`Gender`,`Rating`) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)"
					
					tweet_dic=tweet
					text = tweet_dic["text"].encode('ascii','ignore')
					cor = tweet_dic["cor"] 
					geo =tweet_dic["geo"]
					created_at =  tweet_dic["created_at"]
					sent_pol= tweet_dic["sent_pol"] 
					sent_sub = tweet_dic["sent_sub"]
					gender =  tweet_dic["gender"]
					rate=None
					if(sent_pol >0):
						rate=1
					elif(sent_pol<0):
						rate=-1
					else:
						rate=0



					cursor.execute(sql, (str(name),str(text),str(cor),str(geo),str(created_at),str(sent_pol),str(sent_pol),str(gender),str(rate)))
					connection.commit()
					print("Completed Champions" + str(counter))
					counter+=1
			except Exception as e:
				print(e)
				continue 


def build_db_items(connection):
	client = MongoClient('localhost')
	db = client['LeagueDB']
	collection2=db['Items']


	counter=0
	print("starting")
	for entry in collection2.find():
		dic = entry
		name = dic["name"]
		tweet_list = dic["tweet_list"]

		for tweet in tweet_list:
			try:
				with connection.cursor() as cursor:
					sql = "INSERT INTO `ItemsTwitter` (`Item_Name`, `Tweet_Text`,`Coor`,`Geo`,`Created_At`,`Sent_Pol`,`Sent_Sub`,`Gender`,`Rating`) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)"  
      
					tweet_dic=tweet
					text = tweet_dic["text"].encode('ascii','ignore')
					cor = tweet_dic["cor"]
					geo =tweet_dic["geo"]
					created_at =  tweet_dic["created_at"]
					sent_pol= tweet_dic["sent_pol"] 
					sent_sub = tweet_dic["sent_sub"]
					gender =  tweet_dic["gender"]
					print(text,gender)
					rate=None
					if(sent_pol >0):
						rate=1
					elif(sent_pol<0):
						rate=-1
					else:
						rate=0



					cursor.execute(sql, (str(name),str(text),str(cor),str(geo),str(created_at),str(sent_pol),str(sent_pol),str(gender),str(rate)))
					connection.commit()
					print("Completed item" + str(counter))
					counter+=1
			except Exception as e:
				print(e)
				continue 


def build_db_reddit(connection):
	print("starting")
	client = MongoClient('localhost')
	db = client['LeagueDB']


	sublist=["leagueoflegends","LoLeventVoDs","summonerschool"]
	other = ['SwainMains', 'JhinMains', 'JarvanIVMains', 'RenektonMains', 'DrMundoMains', 'EzrealMains', 'IreliaMains', 'MalphiteMains', 'Illaoi', 'MorganaMains', 'GalioMains', 'SyndraMains', 'EvelynnMains', 'GragasMains', 'ViktorMains', 'WukongMains', 'XayahMains', 'KennenMains', 'LissandraMains', 'Sivir', 'BardMains', ' CaitlynMains', 'VladimirMains', 'VolibearMains', 'UrgotMains', 'RekSaiMains', 'LeeSinMains', 'VarusMains', 'TheSecretWeapon', 'LeagueofJinx', 'LucianMains', 'ThreshMains', 'TwitchMains', 'TeemoTalk', 'MordekaiserMains', 'RivenMains', 'XerathMains', 'Lux', 'OriannaMains', 'DianaMains', 'ZoeMains', 'HeimerdingerMains', 'YorickMains', 'TristanaMains', 'RumbleMains', 'DirtySionMains', 'ZileanMains', 'Kindred', 'VeigarMains', 'CassiopeiaMains', 'SonaMains', 'GarenMains', 'GnarMains', 'TwistedFateMains', 'GravesMains', 'Aurelion_Sol_Mains', 'ShyvanaMains', 'NocturneMains', 'ZyraMains', 'MissFortuneMains', 'LeonaMains', 'RengarMains', 'AzirMains', 'Shen', 'TaliyahMains', 'FiddlesticksMains', 'HecarimMains', 'JayceMains', 'KatarinaMains', 'FioraMains', 'KalistaMains', 'RyzeMains', 'AsheMains', 'EkkoMains', 'ChoGathMains', 'Kog_Mains', 'MasterYiMains', 'UdyrMains', 'ornnmains', 'PantheonMains', 'TrundleMains', 'OlafMains', 'RakanMains', 'NidaleeMains', 'SorakaMains', 'KarmaMains', 'KassadinMains', 'YasuoMains', 'QuinnMains', 'CamilleMains', 'TaricMains', 'RammusMains', 'Velkoz', 'KaisaMains', 'KayleMains', 'JaxMains', 'AniviaMains', 'BlitzcrankMains', 'MalzaharMains', 'WarwickMains', 'ShacoMains', 'GangplankMains', 'AkaliMains', 'Alistar', 'SkarnerMains', 'LuluMains', 'AhriMains', 'NasusMains', 'DariusMains', 'IvernMains', 'AmumuMains', 'Draven', 'TahmKenchMains', 'ViMains', 'SejuaniMains', 'BrandMains', 'AatroxMains', 'NamiMains', 'VayneMains', 'CorkiMains', 'TalonMains', 'MaokaiMains', 'ZiggsMains', 'NunuMains', 'KhaZixMains', 'SingedMains', 'EliseMains', 'LeblancMains', 'XinZhaoMains', 'FizzMains', 'Janna', 'KarthusMains', 'BraumMains', 'ZedMains', 'PoppyMains', 'KaynMains', 'TryndamereMains', 'NautilusMains']
	sublist=sublist+other
		
	with connection.cursor() as cursor:
		
				for element in sublist:
					print(element)
					try:
						elementt = "Reddit" + str(element)
						collection2=db[elementt]
						sql = "select max(id) from RedditThreads"
						#sql = "select max(id) from Items"
						cursor.execute(sql)
						result = cursor.fetchone()
						comment_counter=0
						print(result)
						if(result[0] is None):
							comment_counter=1;
						else:
							comment_counter=result[0]

						try:
							for redthread in collection2.find():

								entry = redthread
								reddit_id=entry["id"] 
								title=entry["title"].encode('ascii','ignore')
								ups = entry["ups"] 
								downs= entry["downs"] 
								url= entry["url"].encode('ascii','ignore')
								viewcount= entry["viewcount"] 
								name =  entry["name"].encode('ascii','ignore') 
								text = entry["text"].encode('ascii','ignore')
								created = entry["created"]
								created_utc = entry["created_utc"]
								permalink = entry["permalink"]
								comment_list=entry["comment_list"]
								#print title
								sql = "INSERT INTO `RedditThreads` (`subreddit`,`reddit_id`,`Title` , `Body_Text`, `ups`, `downs`, `url`,`viewcount`,`user_name` , `created` , `created_utc` , `permalink`)  VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s,%s,%s)"
								cursor.execute(sql, (str(element),str(reddit_id),str(title),str(text),str(ups),str(downs),str(url),str(viewcount),str(name),str(created),str(created_utc),str(permalink)))
								connection.commit()
								print("Added " + str(title))
								for comment in comment_list:
									temp_comment_dir=comment
									name= temp_comment_dir["name"].encode('ascii','ignore')
									ups = temp_comment_dir["ups"]
									downs = temp_comment_dir["downs"]
									id_red = temp_comment_dir["id"]
									text= temp_comment_dir["text"].encode('ascii','ignore')
									sql = "INSERT INTO `RedditComments` (`id`, `user_name`, `reddit_id`, `ups`,`downs`, `body`)  VALUES (%s, %s,%s, %s,%s, %s)"
									cursor.execute(sql, (str(comment_counter),str(name),str(id_red),str(ups),str(downs),str(text)))
									connection.commit()


								comment_counter+=1

						except Exception as e:
							print(e)
							print("fuck")
							continue
					
					except Exception as e:
						print(e)
						print("fuck1")
						continue


		
	

      


