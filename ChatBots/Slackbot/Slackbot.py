"""
Copyright (c) 2018 Inverse Palindrome
Slackbot - Slackbot.py
https://inversepalindrome.com/
"""


import re
import time
import Slack

from chatterbot import ChatBot


socket_delay = 1
direct_mention_regex = "^<@(|[WU].+?)>(.*)"

slackbot = ChatBot("MathBot", 
               output_adapter="SlackOutputAdapter.SlackOutputAdapter",
               logic_adapters=[
                   {
                       "import_path" : "MathLogicAdapter.MathLogicAdapter"
                   }
              ]
          )

def handle_event(event): 
    Slack.event_type = event.get("type")
    Slack.channel = event.get("channel")
    text = event.get("text")

    if Slack.event_type == "message" and not "subtype" in event:
        handle_message(text)

def handle_message(text):
    user_id, message = parse_direct_mention(text)

    if user_id == Slack.bot_id:
        slackbot.get_response(message)

def parse_direct_mention(text):
    matches = re.search(direct_mention_regex, text)

    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def run_slackbot():
    if Slack.client.rtm_connect():
        while True:
            event_list = Slack.client.rtm_read()

            for event in event_list:   
                handle_event(event)
           
            time.sleep(socket_delay)
       
if __name__ == "__main__":
    run_slackbot()