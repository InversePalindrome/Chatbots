"""
Copyright (c) 2018 Inverse Palindrome
Slackbot - SlackInputAdapter.py
https://inversepalindrome.com/
"""


import re
import Slack

from chatterbot.input import InputAdapter
from chatterbot.conversation import Statement
from UnrecognizedInputException import UnrecognizedInputFormatException


DIRECT_MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

class SlackInputAdapter(InputAdapter):
     def process_input(self, statement):
         matches = re.search(DIRECT_MENTION_REGEX, statement)
         
         user_id, message = (matches.group(1), matches.group(2).strip()) if matches else (None, None)

         if user_id is None or message is None or user_id != Slack.bot_id:
             raise UnrecognizedInputFormatException()

         return Statement(message)


         


