import tweepy


class TwitterSimpleConnector:
	def _getData(self):		
		api = tweepy.API()
		return tweepy.Cursor(api.search,
		                           q="boludoJusto",
		                           rpp=100,
		                           result_type="all",
		                           include_entities=True,
		                           lang="en").items()

if __name__ == '__main__':
	print "test for twitter simple connector"
	tc = TwitterSimpleConnector()
	for tweet in tc._getData():
		print tweet.text
