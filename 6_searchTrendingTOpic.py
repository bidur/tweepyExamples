#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import json



#keys of AppPkr16
consumer_key='7uxGIGQjbSRqvRFWhzK5ydmio'
consumer_secret = 'UNL9OAe68NaWyqwpBDEDVXvpksS0x3ksdfJvlfHfncozwrFyTo'
access_token = '4213955833-8TpiXlB60zfcLw4gIpfPt0jJXLjm8LLm0WoIBQe'
access_token_secret =	'0crJHDGQpN7lCEhsQ6UCkoTslbL16osVeLzI8GGAUL0vh'


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
trends1 = api.trends_place(23424977) # get trends worldwide
#trends2 = api.trends_place(23424977) # get trends USA

print json.dumps(trends1, indent=1) # indent makes the output formatted nicely



# WOE ID = 1 for world
# WOE ID = 	23424911 for Nepal
#WOE ID = 2269173  for Pokhara
# WOE ID = 23424977 for US
#  The Yahoo! Where On Earth ID of the location to return trending information for. 
# Global information is available by using 1 as the WOEID.


#print trends1 # prints all data in randomly ( unstructured in a huge JSON string)

# trends1 is a list with only one element in it, which is a 
# dict which we'll put in data.
##data = trends1[0]
# grab the trends
##trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends1]
# put all the names together with a ' ' separating them
trendsName = ' '.join(names)
print(trendsName)


#http://stackoverflow.com/questions/21203260/python-get-twitter-trends-in-tweepy-and-parse-json

# api.trends_place() is defined in http://docs.tweepy.org/en/v3.5.0/api.html  
