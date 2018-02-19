import tweepy
import time
import random

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# friends = api.friends_ids()

# for i, x in enumerate(friends):
	# print(i,x)
	
# for i,follower in enumerate(tweepy.Cursor(api.followers,id="@aimeexvillar").items()):
	# try:
		# if(follower.id) in friends:
			# print("Already Added")
		# else:
			# follower.follow()
			# print(follower.screen_name)
			# time.sleep(5)
		# print(i)	
	# except:
		# pass

with open('output.txt','r') as Quotes:
	for quotes in Quotes:
		if not len(quotes)>140:
			try:
				print("Tweeted: {}".format(quotes))
				api.update_status(quotes)
				x=3600+random.randint(0,7200)
				print(x//60)
				time.sleep(x)
			except:
				pass

