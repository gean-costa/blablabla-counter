import os
import tweepy


class User:
    def __init__(self, screen_name: str) -> None:
        auth = tweepy.OAuthHandler(os.getenv('API_KEY'),
                                   os.getenv('API_KEY_SECRET'))
        auth.set_access_token(os.getenv('ACCESS_TOKEN'),
                              os.getenv('ACCESS_TOKEN_SECRET'))

        self.screen_name = screen_name
        self.api = tweepy.API(auth)
        self.tweets_collection = []

    def get_tweets(self):
        tweets = self.api.user_timeline(
            screen_name=self.screen_name,
            tweet_mode='extended',
            include_rts=False,
            count=200
        )
        tweets_data = [tweet._json for tweet in tweets]
        self.tweets_collection = tweets_data.copy()
        print(
            f"Coletando {len(tweets_data)} tweets. {len(self.tweets_collection)} tweets coletados")

        while(len(tweets) != 0):
            try:
                tweets = self.api.user_timeline(
                    screen_name=self.screen_name,
                    tweet_mode="extended",
                    include_rts=False,
                    count=200,
                    max_id=tweets[len(tweets)-1]._json['id']-1
                )

                if (len(tweets) == 0):
                    break
                else:
                    tweets_data = [tweet._json for tweet in tweets]
                    self.tweets_collection = self.tweets_collection + tweets_data
                    print(
                        f"Coletando {len(tweets_data)} tweets. {len(self.tweets_collection)} tweets coletados")

            except tweepy.RateLimitError as error:
                print(f"Erro: {error}")
                break
