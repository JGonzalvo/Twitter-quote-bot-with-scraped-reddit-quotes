import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'TBzgPOm1Jbio3cjNB77BZWfvQ'
consumer_secret = '0xO1QenDKKokjlYATrpkng6KkH61bsIFcaOW1FGHaSx74BMnIG'
access_token = '910400857010618369-I6Wh9U9aw3XsullzXRPJYkhsMASGkMK'
access_token_secret = 'emxvPJrwK5BBJ3R3Lqc6EBZcLFedgySuHchsWof2OasDC'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('quotes.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#quotes'])