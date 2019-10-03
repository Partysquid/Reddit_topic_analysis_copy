import tweepy
import time
from textblob import TextBlob
from pymongo import MongoClient
import gender_guesser.detector as gender
from threading import Thread
from riotwatcher import RiotWatcher
import pymysql.cursors
import pymysql
class consume:
	def __init__(self,connection):

		auth = tweepy.OAuthHandler('2XAQTR3zNwrBtD2i6AGxZDeP6','7e9xsaOSvyyI0nY5ZDN1cYx0phndLtclhdxukaC1rSjztsH9Q2')
		auth.set_access_token('3333417351-X483ie45LpKqy6vw3LEUa84LN1bG6aMuZXRUlF7', 'FQnPzJbLjvODZXiph48eb5bK2UJRHhjdhBw5thKDFvZer')
		self.api = tweepy.API(auth)
		self.gen = gender.Detector()
		my_region = 'na1'
		watcher = RiotWatcher('RGAPI-11ab2328-9ef7-47f8-a4c5-e4afcf0baab0')
		static_champ_list = watcher.static_data.champions(my_region)
		static_item_list = watcher.static_data.items(my_region)
		champion_list = static_champ_list['data']
		item_list = static_item_list['data']
		item_names=[]
		champion_names=[]
		champion_key_list=list(champion_list.keys())
		item_key_list=list(item_list.keys())
		for i in item_key_list:
			item_names.append(item_list[i]['name'].encode('ascii', 'ignore'))
			

		for i in champion_key_list:
			champion_names.append(champion_list[i]['name'].encode('ascii', 'ignore'))
		self.item_name = item_names
		self.champions_name = champion_names

		print(item_names)
		print(champion_names)
		#coordinates
		self.connection = connection

	def consume_items(self):
		print self.api.rate_limit_status()['resources']['search']['/search/tweets']['remaining'] 
		connection = self.connection
		with connection.cursor() as cursor:
			try:
				item_name=self.item_name
				for i in range(0,len(item_name)):
					current_item=item_name[i]
					while(self.api.rate_limit_status()['resources']['search']['/search/tweets']['remaining'] <30):
						print "Waiting: ITEMS"
						time.sleep(60)
					query = current_item
					for tweet_info in tweepy.Cursor(self.api.search, q=query, lang = 'en', tweet_mode='extended').items(100):
						
						if 'retweeted_status' in dir(tweet_info):
						    continue
						    #tweet=tweet_info.retweeted_status.full_text
						    #print dir(tweet.retweeted_status)
						else:
						    tweet=tweet_info.full_text
						tweet_dic={}
						tweet_dic["text"]=tweet.encode('ascii','ignore')
						tweet_dic["cor"] = tweet_info.coordinates
						tweet_dic["geo"] = tweet_info.geo
						tweet_dic["created_at"] = tweet_info.created_at
						blob = TextBlob(tweet)
						tweet_dic["sent_pol"] = blob.sentiment.polarity
						tweet_dic["sent_sub"] = blob.sentiment.subjectivity
						name=tweet_info.user.name
						tweet_dic["gender"] = self.gen.get_gender(name)
						rate=None
						
						if(tweet_dic["sent_pol"]>0):
							rate=1
						elif(tweet_dic["sent_pol"]<0):
							rate=-1
						else:
							rate = 0
						
						sql = "INSERT INTO `ItemsTwitter` (`Item_Name`, `Tweet_Text`, `Coor`, `Geo`, `Created_At`,`Sent_Pol`,`Sent_Sub`, `Gender`,`Rating`)  VALUES (%s, %s,%s, %s,%s, %s,%s,%s, %s)"
						
						cursor.execute(sql, (str(current_item),str(tweet_dic["text"]),str(tweet_dic["cor"]),str(tweet_dic["geo"]),str(tweet_dic["created_at"]),str(tweet_dic["sent_pol"]),str(tweet_dic["sent_sub"]),str(tweet_dic["gender"]),str(rate)))
						connection.commit()
						print "Post for " + str(item_name[i])
			except Exception as e:
				print(e)
				pass







	def consume_champions(self):
		print self.api.rate_limit_status()['resources']['search']['/search/tweets']['remaining'] 
		connection= self.connection
		with connection.cursor() as cursor:
			try:
				champions_name=self.champions_name
				for i in range(0,len(champions_name)):
					current_item=champions_name[i]
					while(self.api.rate_limit_status()['resources']['search']['/search/tweets']['remaining'] <30):
						print "Waiting: CHAMPIONS"
						time.sleep(60)
					query = current_item
					for tweet_info in tweepy.Cursor(self.api.search, q=query, lang = 'en', tweet_mode='extended').items(100):
						#print dir(tweet_info)
						if 'retweeted_status' in dir(tweet_info):
							continue
						    #tweet=tweet_info.retweeted_status.full_text
						else:
						    tweet=tweet_info.full_text
						tweet_dic={}
						tweet_dic["text"]=tweet.encode('ascii','ignore')
						tweet_dic["cor"] = tweet_info.coordinates
						tweet_dic["geo"] = tweet_info.geo
						tweet_dic["created_at"] = tweet_info.created_at
						blob = TextBlob(tweet)
						tweet_dic["sent_pol"] = blob.sentiment.polarity
						tweet_dic["sent_sub"] = blob.sentiment.subjectivity
						name=tweet_info.user.name
						tweet_dic["gender"] = self.gen.get_gender(name)
						rate=None
						if(tweet_dic["sent_pol"]>0):
							rate=1
						elif(tweet_dic["sent_pol"]<0):
							rate=-1
						else:
							rate = 0

						sql = "INSERT INTO `ChampionsTwitter` (`Champion_Name`, `Tweet_Text`, `Coor`, `Geo`, `Created_At`,`Sent_Pol`,`Sent_Sub`, `Gender`,`Rating`)  VALUES (%s, %s,%s, %s,%s, %s,%s,%s, %s)"
						
						cursor.execute(sql, (str(current_item),str(tweet_dic["text"]),str(tweet_dic["cor"]),str(tweet_dic["geo"]),str(tweet_dic["created_at"]),str(tweet_dic["sent_pol"]),str(tweet_dic["sent_sub"]),str(tweet_dic["gender"]),str(rate)))
						connection.commit()
						print "Post for " + str(champions_name[i])
			except Exception as e:
				print(e)
				pass
	def build_query(self,term_list):
		query=""
		for i in range(0,len(term_list)):
			if(i==len(term_list)-1):
				query = query + str(term_list[i])
			else:
				query = query + term_list[i] + " OR "

		return query
	def thread_go(self):
		t1 = Thread(target=self.consume_items)
		t2 = Thread(target=self.consume_champions)

		t1.start()
		t2.start()
	def run_prog(self):
		while True:
			try:
				self.consume_items()
				self.consume_champions()
			except:
				pass
			




'''
testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
>>> testimonial.sentiment
Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
>>> testimonial.sentiment.polarity
0.39166666666666666
'''

# #You can check how many queries you have left using rate_limit_status() method
# api.rate_limit_status()['resources']['search']


# results = api.search(q=query, lang=language, count=tweetCount, tweet_mode='extended')
# for tweet in results:
#         print(tweet.full_text)


#http://riot-watcher.readthedocs.io/en/latest/riotwatcher/StaticDataApiV3.html#riotwatcher._apis.StaticDataApiV3


# from riotwatcher import RiotWatcher

# watcher = RiotWatcher('<your-api-key>')

# my_region = 'na1'

# me = watcher.summoner.by_name(my_region, 'pseudonym117')
# print(me)

# # all objects are returned (by default) as a dict
# # lets see if i got diamond yet (i probably didnt)
# my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
# print(my_ranked_stats)

# # Lets some champions
# static_champ_list = watcher.static_data.champions(my_region)
# print(static_champ_list)

# # Error checking requires importing HTTPError from requests

# from requests import HTTPError

# # For Riot's API, the 404 status code indicates that the requested data wasn't found and
# # should be expected to occur in normal operation, as in the case of a an
# # invalid summoner name, match ID, etc.
# #
# # The 429 status code indicates that the user has sent too many requests
# # in a given amount of time ("rate limiting").