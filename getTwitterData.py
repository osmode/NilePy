from twython import Twython
import json
import datetime 
import pymongo
import time

#from twython import TwythonStreamer
#from MyStreamer import MyStreamer

# initialize Mongo database
client = pymongo.MongoClient('localhost',27017)
db = client['master']
twitter_coll = db['twitter']
twitter_coll.ensure_index([('id_num',pymongo.ASCENDING), ('unique',True)] )

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
query_terms = ['morsi']

one_week_ago = datetime.datetime.utcnow() - datetime.timedelta(days=7)

while True:

	for term in query_terms:

		today = datetime.date.today()
		today_str = today.__str__()[0:10]

		results = twitter.search(q=term,since=today_str)

		for q in results['statuses']:
			text = q['text']
			print text
			id_num = q['id']
			retweet_count = q['retweet_count']
			created_at = q['created_at']
			dt = datetime.datetime.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')

			twitter_coll.insert( { 'id':id_num, 'text':text, 'created_at':dt, 'retweet_count':retweet_count } )


		time.sleep(10)
		

