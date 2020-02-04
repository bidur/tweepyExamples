import tweepy, time, sys
from tweepy import OAuthHandler

#enter the corresponding information from your Twitter application:


#keys of AppPkr16
consumer_key='7uxGIGQjbSRqvRFWhzK5ydmio'
consumer_secret = 'UNL9OAe68NaWyqwpBDEDVXvpksS0x3ksdfJvlfHfncozwrFyTo'
access_token = '4213955833-8TpiXlB60zfcLw4gIpfPt0jJXLjm8LLm0WoIBQe'
access_token_secret =	'0crJHDGQpN7lCEhsQ6UCkoTslbL16osVeLzI8GGAUL0vh'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

filename=open("myTweets.txt",'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(10)#Tweet every 15 minutes
