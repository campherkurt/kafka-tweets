
import tweepy
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
        self.kf_producer = KafkaProducer(bootstrap_servers=f'{host}:{port}')

    def send_tweets(self, topic: str, tweets):
        for tweet in tweets:
            json_object = {
                'tweet_text': tweet.text,
                'user_name': tweet.user.name,
                'source_url': tweet.source_url,
                'handle': tweet.user.screen_name
            }
            print(self.kf_producer.send(topic, json_object))

    def cleanup(self):
        pass
