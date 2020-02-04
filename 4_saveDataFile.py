#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import os
import sys

# 1MB = 1024*1024.0 = 1048576
MAX_FILE_SIZE = 1048576 * 1024 # 1 GB


#keys of AppPkr16
consumer_key='7uxGIGQjbSRqvRFWhzK5ydmio'
consumer_secret = 'UNL9OAe68NaWyqwpBDEDVXvpksS0x3ksdfJvlfHfncozwrFyTo'
access_token = '4213955833-8TpiXlB60zfcLw4gIpfPt0jJXLjm8LLm0WoIBQe'
access_token_secret =	'0crJHDGQpN7lCEhsQ6UCkoTslbL16osVeLzI8GGAUL0vh'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        # Open a file to wrtie the tweets
        fo = open("twt.txt", "a+")
        
        # print time.ctime()
        #        print data;
        fo.write( data ); # write data to file
        #close the file
        fo.close()
        #fileSize = os.path.getsize("twt.txt")
        if((os.path.getsize("twt.txt") ) > MAX_FILE_SIZE):
			exit(1)
			   
        
        return True
        

    def on_error(self, status):
        print status
        
    
    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream



if __name__ == '__main__':
	
    fo = open("twt.txt","w")
    fo.write(str(time.ctime())+"\n" )
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
	
    
    
    
    #This line filter Twitter Streams to capture data by the keywords: 'flu', 'cough'
    stream.filter(track=['flu','cough','common cold', 'sneeze', 'head cold','h1n1','swineflu','pneumonia','fever','chills', 'runny nose','Noscapine','Triprolidine','Pseudoephedrine','Oxymetazoline','Chlorpheniramine','Levodropropizine','Benzonatate','Aspirin','Codeine', 'Colistimethate','Guaifenesin','Homatropine','Hydrocodone ','Chlorpheniramine'])
    #stream.filter(track=['manchester united'],locations=[-122.75,36.8,-121.75,37.8])
    

    
