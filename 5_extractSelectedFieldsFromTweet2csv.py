#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os

import sys
#changing-default-encoding-of-python
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

# 1MB = 1024*1024.0 = 1048576
MAX_FILE_SIZE = 1048576 * 1024 * 3 # 3 GB

#Variables that contains the user credentials to access Twitter API 

#keys of AppPkr16
consumer_key='7uxGIGQjbSRqvRFWhzK5ydmio'
consumer_secret = 'UNL9OAe68NaWyqwpBDEDVXvpksS0x3ksdfJvlfHfncozwrFyTo'
access_token = '4213955833-8TpiXlB60zfcLw4gIpfPt0jJXLjm8LLm0WoIBQe'
access_token_secret =	'0crJHDGQpN7lCEhsQ6UCkoTslbL16osVeLzI8GGAUL0vh'




class listener(StreamListener):

    def on_status(self, status):
		       
			
        print "\n\n------------------------------------------"
        latitude=''
        longitude = ''
        data = "\n"+ str(status.id ) 
        print status.text
        
        print "-----------lat/long---------"
        if status.geo is not None:
			latitude, longitude = status.geo['coordinates']
			print 'latitude: ',latitude
			print 'longitude: ', longitude
			
        elif status.place is not None and getattr(status, 'coordinates'):
			longitude, latitude = status.place.coordinates[0][0]
			
			print 'latitude1: ',latitude
			print 'longitude1: ', longitude 
        data += ','+ str(latitude) + ',' +  str(longitude	)
            

		
        print "--------place------------"   
        data += ','
        if status.place:
			data += str(status.place.full_name	)
			print 'place:', status.place.full_name
			
        data += ','
        if status.created_at:			
			data += str(status.created_at)
			print status.created_at		        
        
        tweetTextClean =  (status.text).replace('\n',' ')
        data +=  ","+ (tweetTextClean).replace(',',';')
        
        
        # Open a file to wrtie the extracted  parts of the tweets 
        fo = open("twt.csv", "a+")
        
        #print time.ctime()
        fo.write( data ); # write data to file
        #close the file
        fo.close()
        #fileSize = os.path.getsize("twt.txt")
        if((os.path.getsize("twt.csv") ) > MAX_FILE_SIZE):
			exit(1)				
	
        return True

    on_event = on_status

    def on_error(self, status):
        print status
        


if __name__ == '__main__':
	
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = listener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

 
    #This line filter Twitter Streams to capture data by the keywords: 'flu', 'cough'
    stream.filter(track=['flu','cough','common cold', 'sneeze', 'head cold','h1n1','swineflu','pneumonia','fever','chills', 'runny nose','Noscapine','Triprolidine','Pseudoephedrine','Oxymetazoline','Chlorpheniramine','Levodropropizine','Benzonatate','Aspirin','Codeine', 'Colistimethate','Guaifenesin','Homatropine','Hydrocodone ','Chlorpheniramine'])
    

    
    
   
