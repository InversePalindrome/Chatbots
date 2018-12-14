import os
import time
import re
import slackclient

from chatterbot import ChatBot
from MathLogicAdapter import MathLogicAdapter


socket_delay = 1
direct_mention_regex = "^<@(|[WU].+?)>(.*)"

slack_token = os.environ["SLACK_API_TOKEN"]
slack_client_id = os.environ["SLACK_CLIENT_ID"]
slack_client_secret = os.environ["SLACK_CLIENT_SECRET"]

sc = slackclient.SlackClient(slack_token)

bot_id = sc.api_call("auth.test")["user_id"]

chatbot = ChatBot("MathBot", 
               logic_adapters=[
                   {
                       "import_path" : "MathLogicAdapter.MathLogicAdapter"
                   }
              ]
          )

def handle_event(event): 
    event_type = event.get("type")
    channel = event.get("channel")
    text = event.get("text")

    if event_type == "message" and not "subtype" in event:
        handle_message(channel, text)

def handle_message(channel, text):
    user_id, message = parse_direct_mention(text)

    if user_id == bot_id:
        response = str(chatbot.get_response(message))
        
        sc.api_call("chat.postMessage", text=response, channel=channel)

def parse_direct_mention(text):
    matches = re.search(direct_mention_regex, text)

    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def run_chatbot():
    if sc.rtm_connect():
        while True:
            event_list = sc.rtm_read()

            for event in event_list:   
                handle_event(event)
           
            time.sleep(socket_delay)
       
if __name__ == '__main__':
    run_chatbot()
    