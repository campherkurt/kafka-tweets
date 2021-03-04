
import tweepy
import json

from kafka import KafkaProducer


class TweetFetch:

    def __init__(
        self,
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    ) -> None:

        self.auth = tweepy.OAuthHandler(
            consumer_key,
            consumer_secret
        )
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def get_tweets(self):
        return self.api.home_timeline()


class TweetProd:
    def __init__(self, host: str, port: int) -> None:
        h = f'{host}:{port}'
        self.kf_producer = KafkaProducer(bootstrap_servers=h)

    def send_tweets(self, topic: str, tweets: list) -> None:
        for tweet in tweets:
            json_tweet = self.convert_tweet_to_json(tweet._json)
            self.kf_producer.send(topic, json_tweet)
        self.kf_producer.flush()

    def cleanup(self):
        pass

    def convert_tweet_to_json(self, tweet: dict) -> json:
        return json.dumps(tweet)
