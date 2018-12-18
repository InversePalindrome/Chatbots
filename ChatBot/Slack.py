"""
Copyright (c) 2018 Inverse Palindrome
Chatbot - Slack.py
https://inversepalindrome.com/
"""


import os
import slackclient


token = os.environ["SLACK_API_TOKEN"]
client_id = os.environ["SLACK_CLIENT_ID"]
client_secret = os.environ["SLACK_CLIENT_SECRET"]
client = slackclient.SlackClient(token)

bot_id = client.api_call("auth.test")["user_id"]

event_type = None
channel = None
filename = None
