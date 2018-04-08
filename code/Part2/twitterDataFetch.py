import tweepy
import json
import time
import re
import string
from datetime import date
from tweepy import OAuthHandler
# from nltk.corpus import stopwords
# from nltk.tokenize import TweetTokenizer
# from nltk.stem.wordnet import WordNetLemmatizer
# sw = stopwords.words('english')
# lemma = WordNetLemmatizer()

class TwitterDataCollecion(object):
    
    def __init__(self,query,tweetscount):
        
        #Initialize the twitter api connection
        consumer_key = 'xxxx'
        consumer_secret = 'xxxx'
        access_token = 'xxxx'
        access_secret = 'xxxx'
         
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(auth)
        self.query = query
        self.tcount = tweetscount


    def search_tweet(self):
        ''' Function that takes in a search string 'query', the maximum
            number of tweets 'self.tcount'. It returns a list of 
            tweepy.models.Status objects. '''
     
        searched_tweets = []
        while len(searched_tweets) < self.tcount:
            remaining_tweets = self.tcount - len(searched_tweets)
            try:
                new_tweets = self.api.search(q=self.query, count=remaining_tweets)
                print('found',len(new_tweets),'tweets')
                if not new_tweets:
                    print('no tweets found')
                    break
                searched_tweets.extend(new_tweets)
            except tweepy.TweepError:
                print('exception raised, waiting 1 minutes')
                time.sleep(1*60)
                continue
                #Continue the tweets collection after sleeping for 1 mins
        return searched_tweets
    
    
    def clean_text_and_tokenize(self,line):
        # line   = re.sub(r'\$\w*', '', line)
        # line   = re.sub(r'http?:.*$', '', line)
        # line   = re.sub(r'https?:.*$', '', line)
        # line   = re.sub(r'pic?.*\/\w*', '', line)
        # line   = re.sub(r'[' + string.punctuation + ']+', ' ', line)  # Remove puncutations like 's
        
        tokens = TweetTokenizer(strip_handles=True, reduce_len=True).tokenize(line)
        # tokens = [w.lower() for w in tokens if w not in sw and len(w) > 2 and w.isalpha()]
        # tokens = [lemma.lemmatize(word) for word in tokens]
        
        return tokens

       
    def clean_tweet(self,tweet):
        return " ".join(self.clean_text_and_tokenize(tweet))
    
    
    def write_tweets(self,tweets, filename,encoding="utf-8"):
        ''' Function that appends the cleansed tweets to a file. '''
     
        with open(filename, 'a') as f:
            for tweet in tweets:
                # t = self.clean_tweet(tweet._json["text"])
                t = tweet._json["text"]
                t = str(t.encode("ascii", "ignore"))
                # index = t.find(':')
                f.write(t[t.find(':')+2:-1])
                f.write("\n")

def main():
    query = "fakenews"
    print("Collecting tweets for "+ query)
    today = date.today().strftime("%d%m%y")
    maxtweets = 5000
    twitterclass = TwitterDataCollecion(query,5000)
    tweets=twitterclass.search_tweet()
    twitterclass.write_tweets(tweets, "textcorpus/tweetsdata"+"-"+query+"-"+today+".txt")
    print("Twitter Data is ready for further analysis")
    
if __name__ == '__main__':
    main()
