from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from observable import *
import json

#TODO: hacer una estrategia comun de loggers
level = "DEBUG"

def debug(x):
	if level == "DEBUG":
		print(x)

# Go to http://dev.twitter.com and create an app. 
# The consumer key and secret will be generated for you after
consumer_key="KsMla1PNoIANjKAIYxOAw"
consumer_secret="cxsJEBxeYRNbrQcOT7pKI5dKKzK5GlLQtAtpCn3s"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="220551350-XpcmMVkkA7JojJzoqzhNUSuUS0TJQKigROsz11Pr"
access_token_secret="0YkZTlFw3RqLWEj0JaYEzEkJ1EqDmFd0qMRkBJ2fMO8"

class TwitterStreamingConnector(Observable):
	def __init__(self, hashtag):
		debug("building an instance of the streaming connector")		
		self.observers = []
		self.hashtag = hashtag
		self.startStream()
		debug("instance of the streaming connector successfully created")		
		
	def startStream(self):
		debug("starting up stream")
		l = StdOutListener()
		l.startData(self.observers)
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		stream = Stream(auth, l)	
		stream.filter(track=[self.hashtag], async = True)
	def addObserver(self, observer):
		self.observers.append(observer)


class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream. 
	This is a basic listener that just prints received tweets to stdout.

	"""
	def startData(self,observers):
		self.observers = observers

	def on_data(self, data):				
		jsonData = json.loads(data)
		#TODO data to textableData
		for observer in self.observers:
			observer.update(jsonData['text'])			
		return True

	def on_error(self, status):
		print status

# if __name__ == '__main__':
# 	print "test for twitter streaming connector"
# 	tc = TwitterStreamingConnector()