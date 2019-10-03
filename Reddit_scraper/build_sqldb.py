import pymysql.cursors
import tweepy
import time
from textblob import TextBlob
from pymongo import MongoClient
import gender_guesser.detector as gender
from threading import Thread
def build(connection):
    try:
        conn=connection

        conn.cursor().execute('create database LeagueDB')
    except:
        print("Database LeagueDB exists")


    try:
        with connection.cursor() as cursor:
            # Create a new record
            sqlQuery = "CREATE TABLE ChampionsTwitter(id int UNSIGNED AUTO_INCREMENT PRIMARY KEY, dt_created datetime DEFAULT CURRENT_TIMESTAMP, Champion_Name TEXT, Tweet_Text TEXT, Coor TEXT, Geo TEXT, Created_At TEXT,Sent_Pol DOUBLE,Sent_Sub DOUBLE, Gender TEXT,Rating INT)"   
            cursor.execute(sqlQuery)
            connection.commit()
            print("Finished Building Champions")
    except:
    	print("Tables Champions Exist")


    try:
        with connection.cursor() as cursor:
            # Create a new record
            sqlQuery = "CREATE TABLE ItemsTwitter(id int UNSIGNED AUTO_INCREMENT PRIMARY KEY,dt_created datetime DEFAULT CURRENT_TIMESTAMP, Item_Name TEXT, Tweet_Text TEXT, Coor TEXT, Geo TEXT, Created_At TEXT,Sent_Pol DOUBLE,Sent_Sub DOUBLE, Gender TEXT,Rating INT)"   
            cursor.execute(sqlQuery)
            connection.commit()
            print("Finished Building Items")
    except:
        print("Tables Items Already Exist")



    sublist=["leagueoflegends","LoLeventVoDs","summonerschool"]
    other = ['SwainMains', 'JhinMains', 'JarvanIVMains', 'RenektonMains', 'DrMundoMains', 'EzrealMains', 'IreliaMains', 'MalphiteMains', 'Illaoi', 'MorganaMains', 'GalioMains', 'SyndraMains', 'EvelynnMains', 'GragasMains', 'ViktorMains', 'WukongMains', 'XayahMains', 'KennenMains', 'LissandraMains', 'Sivir', 'BardMains', ' CaitlynMains', 'VladimirMains', 'VolibearMains', 'UrgotMains', 'RekSaiMains', 'LeeSinMains', 'VarusMains', 'TheSecretWeapon', 'LeagueofJinx', 'LucianMains', 'ThreshMains', 'TwitchMains', 'TeemoTalk', 'MordekaiserMains', 'RivenMains', 'XerathMains', 'Lux', 'OriannaMains', 'DianaMains', 'ZoeMains', 'HeimerdingerMains', 'YorickMains', 'TristanaMains', 'RumbleMains', 'DirtySionMains', 'ZileanMains', 'Kindred', 'VeigarMains', 'CassiopeiaMains', 'SonaMains', 'GarenMains', 'GnarMains', 'TwistedFateMains', 'GravesMains', 'Aurelion_Sol_Mains', 'ShyvanaMains', 'NocturneMains', 'ZyraMains', 'MissFortuneMains', 'LeonaMains', 'RengarMains', 'AzirMains', 'Shen', 'TaliyahMains', 'FiddlesticksMains', 'HecarimMains', 'JayceMains', 'KatarinaMains', 'FioraMains', 'KalistaMains', 'RyzeMains', 'AsheMains', 'EkkoMains', 'ChoGathMains', 'Kog_Mains', 'MasterYiMains', 'UdyrMains', 'ornnmains', 'PantheonMains', 'TrundleMains', 'OlafMains', 'RakanMains', 'NidaleeMains', 'SorakaMains', 'KarmaMains', 'KassadinMains', 'YasuoMains', 'QuinnMains', 'CamilleMains', 'TaricMains', 'RammusMains', 'Velkoz', 'KaisaMains', 'KayleMains', 'JaxMains', 'AniviaMains', 'BlitzcrankMains', 'MalzaharMains', 'WarwickMains', 'ShacoMains', 'GangplankMains', 'AkaliMains', 'Alistar', 'SkarnerMains', 'LuluMains', 'AhriMains', 'NasusMains', 'DariusMains', 'IvernMains', 'AmumuMains', 'Draven', 'TahmKenchMains', 'ViMains', 'SejuaniMains', 'BrandMains', 'AatroxMains', 'NamiMains', 'VayneMains', 'CorkiMains', 'TalonMains', 'MaokaiMains', 'ZiggsMains', 'NunuMains', 'KhaZixMains', 'SingedMains', 'EliseMains', 'LeblancMains', 'XinZhaoMains', 'FizzMains', 'Janna', 'KarthusMains', 'BraumMains', 'ZedMains', 'PoppyMains', 'KaynMains', 'TryndamereMains', 'NautilusMains']
    sublist=sublist+other



    try:
        with connection.cursor() as cursor:
            # Create a new record
            sqlQuery = "CREATE TABLE RedditThreads(id int UNSIGNED AUTO_INCREMENT PRIMARY KEY,dt_created datetime DEFAULT CURRENT_TIMESTAMP, subreddit TEXT, reddit_id TEXT,Title TEXT, Body_Text LONGTEXT, ups INT, downs INT, url TEXT, viewcount TEXT, user_name TEXT, created TEXT, created_utc TEXT, permalink TEXT )"   
            cursor.execute(sqlQuery)
            connection.commit()
            print("Finished Building RedditThreads")
    except:
        print("RedditThreads already exist")



    try:
        with connection.cursor() as cursor:
            # Create a new record
            sqlQuery = "CREATE TABLE RedditComments(dt_created datetime DEFAULT CURRENT_TIMESTAMP,id int UNSIGNED, user_name TEXT, reddit_id TEXT, ups INT, downs INT, body TEXT, created TEXT, created_utc TEXT)" 
            cursor.execute(sqlQuery)
            connection.commit()
            print("Finished Building RedditComment")
    except:
        print("RedditComment already exist")

