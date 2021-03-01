# Access Token:   20007529-4c0mqw376oqBEm6JuozKCjDy1htiohDi07SzqnGGi
# Token Secret:   wzj4FdKItMw5GPedQtjp0MetGfPPNrPg4XuS3zRE4UBgh
# API Key:        idjtqLOZ43ev5LOmveIAQ
# API Secret Key: P3fCnTAH3Q57jEHUyGyLZN4RMWnQ1UkPGba1c1WquM

'''
Class that takes a list of topics and fetches the posts.

'''
import tweepy

consumer_key = 'idjtqLOZ43ev5LOmveIAQ'
consumer_secret = 'P3fCnTAH3Q57jEHUyGyLZN4RMWnQ1UkPGba1c1WquM'
access_token = '20007529-4c0mqw376oqBEm6JuozKCjDy1htiohDi07SzqnGGi'
access_token_secret = 'wzj4FdKItMw5GPedQtjp0MetGfPPNrPg4XuS3zRE4UBgh'


def get_tweets(api):
    public_tweets = api.home_timeline()
    print(f"Tweet amount: {len(public_tweets)}")
    return public_tweets


def get_twitter_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api
