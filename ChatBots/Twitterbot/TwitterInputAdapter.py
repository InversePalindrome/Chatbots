"""
Copyright (c) 2018 Inverse Palindrome
Twitterbot - TwitterInputAdapter.py
https://inversepalindrome.com/
"""


from chatterbot.input import InputAdapter
from chatterbot.conversation import Statement


class TwitterInputAdapter(InputAdapter):
    def process_input(self, statement):
        return Statement("Hello")


