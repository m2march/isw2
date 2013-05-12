import tweepy
from observable import *

class TwitterSimpleConnector(Observable):
	def __init__(self,hashtag):
		self.hashtag = hashtag
		self.observers = []
	
	def addObserver(self, observer):
		self.observers.append(observer)

	def pull(self):		
		api = tweepy.API()
		tweets =  tweepy.Cursor(api.search,
		                           q=self.hashtag,
		                           rpp=300,
		                           result_type="recent",
		                           include_entities=True,
		                           lang="es").items()
		for observer in self.observers:
			for tweet in tweets:
				observer.update(tweet)
		return tweets



if __name__ == '__main__':
	print "test for twitter simple connector"
	tc = TwitterSimpleConnector()
	for tweet in tc.pull():		
		print tweet.text.encode('utf-8','ignore')
