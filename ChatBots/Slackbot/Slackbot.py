"""
Copyright (c) 2018 Inverse Palindrome
Slackbot - Slackbot.py
https://inversepalindrome.com/
"""


import time
import Slack

from chatterbot import ChatBot
from UnrecognizedInputException import UnrecognizedInputFormatException


SOCKET_DELAY = 1

slackbot = ChatBot("MathBot", 
               input_adapter = "SlackInputAdapter.SlackInputAdapter",
               output_adapter = "SlackOutputAdapter.SlackOutputAdapter",
               logic_adapters = [
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
        try:
            slackbot.get_response(text)
        except UnrecognizedInputFormatException:
            print("Unrecognized input format!")

def run_slackbot():
    if Slack.client.rtm_connect():
        while True:
            event_list = Slack.client.rtm_read()

            for event in event_list:   
                handle_event(event)
           
            time.sleep(SOCKET_DELAY)
       
if __name__ == "__main__":
    run_slackbot()