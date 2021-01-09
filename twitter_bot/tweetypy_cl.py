import sys
from dotenv import load_dotenv
from pathlib import Path
import os
import tweepy
import time
import piglatin


try:
    #Topic
    topic = sys.argv[1]

    #Env File
    load_dotenv()
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    #Keys and Tokens
    API_KEY = os.getenv("API_KEY")
    API_SECRET_KEY = os.getenv("API_SECRET_KEY")
    TOKEN = os.getenv("TOKEN")
    SECRET_TOKEN = os.getenv("SECRET_TOKEN")

    #Authentication with Twitter API
    auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
    auth.set_access_token(TOKEN, SECRET_TOKEN)

    api = tweepy.API(auth)

    def find_tweets(topic):
        return tweepy.Cursor(api.search, topic).items(10)

    def translate_tweets(tweets):
        translated_tweets = []
        for tweet in tweets:
            text = tweet.text
            translated = piglatin.translate(text)
            translated_tweets.append(translated)
        return translated_tweets

    def print_tweets(tweets):
        for tweet in tweets:
            print(tweet + '\n')

    def main():
        tweets = find_tweets(topic)
        translated_tweets = translate_tweets(tweets)
        print_tweets(translated_tweets)


    if __name__=='__main__':
        main()

except IndexError as err:
    print(err)