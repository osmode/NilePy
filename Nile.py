from twython import TwythonStreamer
from MyStreamer import MyStreamer

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
stream.statuses.filter(track='mursi,moursy,morsy,morsi,mursy,moursi',location='30.3,31.14,30.050,31.233')


