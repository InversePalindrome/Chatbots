"""
Copyright (c) 2018 Inverse Palindrome
Chatbot - SlackOutputAdapter.py
https://inversepalindrome.com/
"""


import Slack

from chatterbot.output import OutputAdapter


class SlackOutputAdapter(OutputAdapter):
    def process_response(self, statement, conversation_id):
        Slack.client.api_call("chat.postMessage", text=statement.text, channel=Slack.channel)
        
        return statement

