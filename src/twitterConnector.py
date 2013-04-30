from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://dev.twitter.com and create an app. 
# The consumer key and secret will be generated for you after
consumer_key="KsMla1PNoIANjKAIYxOAw"
consumer_secret="cxsJEBxeYRNbrQcOT7pKI5dKKzK5GlLQtAtpCn3s"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="220551350-XpcmMVkkA7JojJzoqzhNUSuUS0TJQKigROsz11Pr"
access_token_secret="0YkZTlFw3RqLWEj0JaYEzEkJ1EqDmFd0qMRkBJ2fMO8"


class TwitterStreamingConnector:
	def __init__(self):
		self.__tweets__= list()
		print "se ejecuto el constructor"
	def __getData__(self):
		print "se ejecuto getData"
		return self.__tweets__
	def startStream(self):
		print "starteando el stream"
		l = StdOutListener()
		l.startData(self.__tweets__)
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		stream = Stream(auth, l)	
		stream.filter(track=['#boludoJusto'], async = True)


class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream. 
	This is a basic listener that just prints received tweets to stdout.

	"""
	def startData(self,tweets):
		self.database = tweets

	def on_data(self, data):		
		print data
		self.database.append(data)
		return True

	def on_error(self, status):
		print status

# if __name__ == '__main__':
# 	l = StdOutListener()
# 	auth = OAuthHandler(consumer_key, consumer_secret)
# 	auth.set_access_token(access_token, access_token_secret)

# 	stream = Stream(auth, l)	
# 	stream.filter(track=['#boludoJusto'])