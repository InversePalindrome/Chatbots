"""
Copyright (c) 2018 Inverse Palindrome
Twitterbot - Twitterbot.py
https://inversepalindrome.com/
"""


import time

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


twitterbot = ChatBot(
    "Twitterbot",
    input_adapter = "TwitterInputAdapter.TwitterInputAdapter",
    output_adapter = "TwitterOutputAdapter.TwitterOutputAdapter")

twitterbot.set_trainer(ChatterBotCorpusTrainer)
       
twitterbot.train("chatterbot.corpus.english.greetings")

def run_twitterbot():
    while True:
        twitterbot.get_response("Hello")
        time.sleep(6000)

if __name__ == "__main__":
    run_twitterbot()