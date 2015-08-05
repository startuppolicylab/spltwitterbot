#TIPS: To turn bot on heroku ps:scale worker=1
#To turn bot off heroku ps:scale worker=0

import tweepy, time
from datetime import datetime
from pytz import timezone
import pytz
from tzlocal import get_localzone
import random_phrase as phraseGen
import random

hour = 60*60
halfHour = 30*60
threehour = 3*hour
twentymin = 20*60

def currentTime():
	tz = timezone('America/Los_Angeles')
	utc = pytz.utc
	pacificTime = datetime.now(tz)
	return pacificTime

CONSUMER_KEY = 'fyCGfXiAg6bUy7EAiye5Gtjm4'
CONSUMER_SECRET = 'njP2SLGmuzvnge42g8J2m1jBHdzpmUqOVLbr8kojcPQs6wrrcT' # Make sure access level is Read And Write in the Settings tab
ACCESS_KEY = '283429527-8n97CE26tfAmA1YxF4c8ebpZG9wrWQg8l5JOueL4'
ACCESS_SECRET = 'dpLwy9SXfPlsmPVT3IKmofoh4yzW30k9GioQmB1bciHc4'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)




#////////////////
#Make sure you debug the file reading
#////////////////
filename=open('words.txt','r')
f=filename.readlines()
filename.close()


#Project Proposal: Send tweets from SPL account 
#every 3 hours between the hours of 6AM PST & 3PM PST. 
for line in f:
#	currH = currentHour()
	print "New line"
	while (currentTime().hour < 6) or (currentTime().hour > 15):
		time.sleep(threehour)
	if (currentTime().hour == 12):
		foo = phraseGen.random_word()
		phrase = phraseGen.random_phrase(random.randint(1,6), foo)
		if len(phrase) > 140:
			continue
		api.update_status(phrase)
		print phrase
	api.update_status(line)
	print line 
	print currentTime().hour
	time.sleep(threehour)




#----------------
#BELOW CODE WRITTEN FOR EASE OF DEBUGGING. SET TO A 30 SECOND INTERVAL!
#----------------

# api.update_status("hello")

# counter = 0;
# for line in f:
# 	api.update_status(line)
# 	time.sleep(30) #sleep for 30 seconds
# 	counter += 1
# 	if counter > 2:
#		break