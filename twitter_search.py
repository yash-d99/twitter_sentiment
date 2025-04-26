import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth, wait_on_rate_limit=True)
def search_tweets(query, num_tweets=1):
    filtered = []
    tweets = api.search_tweets(q=query, count=num_tweets, tweet_mode='extended')
    unfiltered = [{'text': tweet.full_text, 'created_at': tweet.created_at} for tweet in tweets]
    for tweet in unfiltered:
        filtered.append(tweet['text'])
    return filtered


# if __name__ == "__main__":
#     query = "happy"
#     tweets = search_tweets(query, num_tweets =1)
#     print(tweets)

