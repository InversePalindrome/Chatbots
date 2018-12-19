"""
Copyright (c) 2018 Inverse Palindrome
Twitterbot - Twitter.py
https://inversepalindrome.com/
"""


import os
import tweepy


consumer_key = os.environ["TWITTER_CONSUMER_KEY"],
consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"],
access_token = os.environ["TWITTER_ACCESS_TOKEN"],
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

API = tweepy.API(auth)