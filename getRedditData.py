# This script demonstrates how to query the reddit API and populate a 
# MongoDB database with the results. Most of this code was written by
# Tankor Smash: blog.tankorsmash.com/?p=295
# The only novelty I introduce here is how to populate a MongoDB database
# Remember to fill in your reddit username and password in 'user_pass_dict'

import requests, json, time, sys
from pymongo import MongoClient

query_term = 'morsi'

user_pass_dict = {'user': '', 'passwd': '', 'api_type':'json'}

s = requests.Session()
s.headers.update({'User-Agent':'short_description_of_yourself user:osmode'})
r = s.post(r'http://www.reddit.com/api/login',data=user_pass_dict)
j = json.loads(r.content)
after = "" # used to retrieve additional queries in case max limit
	   # is exceeded

# populate mongo database named 'reddit'
client = MongoClient('localhost',27017)
db = client['reddit']
posts = db['posts']

while True:
	time.sleep(10)
	try:
		url = "http://www.reddit.com/r/all/new/.json?q="+query_term+"&limit=100&sort=new&after="+after
		html = s.get(url)
		if html.status_code != 200:
			sys.stderr.write(str(html.status_code))
			sys.stderr.write(url)
			continue
		# convert string into json object
		json_obj = json.loads(html.content)
		print json_obj
		# insert content into database
		post_id = posts.insert(json_obj)
		after = json_obj['data']['after']

	except:
		pass


