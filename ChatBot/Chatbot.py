import os
import slackclient

slack_token = os.environ["SLACK_API_TOKEN"]
sc = slackclient.SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#general",
  text="Hi, I am Euler!"
)