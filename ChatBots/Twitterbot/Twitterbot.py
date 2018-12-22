"""
Copyright (c) 2018 Inverse Palindrome
Twitterbot - Twitterbot.py
https://inversepalindrome.com/
"""


import time
import pyjokes

from Twitter import API
from chatterbot import ChatBot


twitterbot = ChatBot(
    "Twitterbot")
    
def run_twitterbot():
    while True:
        API.PostUpdate(pyjokes.get_joke(category = "all"))

        time.sleep(3600)
    
if __name__ == "__main__":
    run_twitterbot()