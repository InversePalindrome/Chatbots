"""
Copyright (c) 2018 Inverse Palindrome
Twitterbot - Twitterbot.py
https://inversepalindrome.com/
"""


from chatterbot import ChatBot


twitterbot = ChatBot(
    "Twitterbot",
    logic_adapters = [
        "chatterbot.logic.BestMatch"
    ],
    trainer = "TwitterTrainer.TwitterTrainer")
       
twitterbot.train()

if __name__ == "__main__":
    twitterbot.train()