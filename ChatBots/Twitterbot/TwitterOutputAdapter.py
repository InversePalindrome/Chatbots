"""
Copyright (c) 2018 Inverse Palindrome
Twitterbot - TwitterOutputAdapter.py
https://inversepalindrome.com/
"""


from Twitter import API
from chatterbot.output import OutputAdapter


class TwitterOutputAdapter(OutputAdapter):
    def process_response(self, statement, session_id = None):
        API.update_status(statement.text)
        
        return statement
        


