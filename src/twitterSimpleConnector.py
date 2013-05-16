import tweepy
#from observable import *

class TwitterSimpleConnector:
	def __init__(self,hashtag, language="es"):
		self.language = language
		self.hashtag = hashtag
		self.observers = []

	def getData(self):
		api = tweepy.API()
		tweets =  tweepy.Cursor(api.search,
		                           q=self.hashtag,
		                           rpp=300,
		                           result_type="recent",
		                           include_entities=True,
		                           lang=self.language).items()
		return tweets

if __name__ == '__main__':
	print "test for twitter simple connector"
	tc = TwitterSimpleConnector("#precioJusto","es")
	for tweet in tc.getData():
		print tweet.text.encode('utf-8','ignore')
