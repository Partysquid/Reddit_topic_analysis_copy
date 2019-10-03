import os
import time

def build_db():

	os.chdir(os.getcwd()+"/jsonstufftwitter")
	vals= os.listdir(os.getcwd())
	for val in vals:
		if "json" in val:
			splits = val.split('.')
			collection = splits[0]
			os.system("mongoimport --db LeagueDB" +  " --collection " + collection + " --file " + collection +".json --jsonArray")
	print("Done with Twitter")
	os.chdir("..")
	os.chdir(os.getcwd()+"/jsonstuffreddit")
	vals= os.listdir(os.getcwd())
	for val in vals:
		if "json" in val:
			splits = val.split('.')
			collection = splits[0]
			os.system("mongoimport --db LeagueDB" +  " --collection " + collection + " --file " + collection +".json --jsonArray")
	print("Done with Reddit")
	

