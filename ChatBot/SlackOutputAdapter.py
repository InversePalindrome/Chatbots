"""
Copyright (c) 2018 Inverse Palindrome
Chatbot - SlackOutputAdapter.py
https://inversepalindrome.com/
"""


import Slack

from chatterbot.output import OutputAdapter


class SlackOutputAdapter(OutputAdapter):
    def process_response(self, statement, conversation_id):
        Slack.client.api_call("chat.postMessage", text = statement.text, channel = Slack.channel)

        if Slack.filename is not None:
            with open(Slack.filename, 'rb') as file_content:
                Slack.client.api_call("files.upload", channels = Slack.channel, file=file_content)

        Slack.event_type = None
        Slack.channel = None
        Slack.filename = None
        
        return statement

