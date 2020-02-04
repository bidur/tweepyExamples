#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#keys of AppPkr16
consumer_key='7uxGIGQjbSRqvRFWhzK5ydmio'
consumer_secret = 'UNL9OAe68NaWyqwpBDEDVXvpksS0x3ksdfJvlfHfncozwrFyTo'
access_token = '4213955833-8TpiXlB60zfcLw4gIpfPt0jJXLjm8LLm0WoIBQe'
access_token_secret =	'0crJHDGQpN7lCEhsQ6UCkoTslbL16osVeLzI8GGAUL0vh'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print "data: ",
        print data
        return True

    def on_error(self, status):
        print "status: ",
        print status

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: #nepal
    stream.filter(track=['#visitnepal2020',"#nepal"])
