import urllib, json
import sys
import tweepy
from tweepy import OAuthHandler

#keys of AppPkr16
consumer_key='7uxGIGQjbSRqvRFWhzK5ydmio'
consumer_secret = 'UNL9OAe68NaWyqwpBDEDVXvpksS0x3ksdfJvlfHfncozwrFyTo'
access_token = '4213955833-8TpiXlB60zfcLw4gIpfPt0jJXLjm8LLm0WoIBQe'
access_token_secret =	'0crJHDGQpN7lCEhsQ6UCkoTslbL16osVeLzI8GGAUL0vh'
 # API described at https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline

def twitter_fetch(screen_name = "BBCNews",maxnumtweets=10):
    print 'Fetch tweets from @BBCNews'
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
	
    #print api.me().name
    #api.update_status('Hello -tweepy + oauth!')

    for status in tweepy.Cursor(api.user_timeline,id=screen_name).items(10): 
        print status.text+'\n'

   

if __name__ == '__main__':
    twitter_fetch('BBCNews',10)


#http://techno-sups.blogspot.com/2013/06/tweepy-get-users-timeline-status-from.html
# Cursor Details: http://docs.tweepy.org/en/v3.5.0/cursor_tutorial.html
