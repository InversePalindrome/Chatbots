import os
import time
import slackclient

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

socket_delay = 1

slack_token = os.environ["SLACK_API_TOKEN"]
slack_client_id = os.environ["SLACK_CLIENT_ID"]
slack_client_secret = os.environ["SLACK_CLIENT_SECRET"]

sc = slackclient.SlackClient(slack_token)

bot_id = sc.api_call("auth.test")["user_id"]

chatbot = ChatBot("Tycho")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english")

def handleEvent(event):
    user_id = event.get("user")
    channel = event.get("channel")
    text = event.get("text")
  
    if user_id and channel and text:
        handleMessage(channel, text)

def handleMessage(channel, text):
    response = str(chatbot.get_response(text))
    
    sc.api_call("chat.postMessage", text=response, channel=channel)

def runChatbot():
    if sc.rtm_connect():
        while True:
            event_list = sc.rtm_read()

            for event in event_list:   
               handleEvent(event)
           
            time.sleep(socket_delay)
       

if __name__ == '__main__':
    runChatbot()
    