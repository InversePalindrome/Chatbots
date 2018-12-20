"""
Copyright (c) 2018 Inverse Palindrome
Slackbot - UnrecognizedInputException.py
https://inversepalindrome.com/
"""


class UnrecognizedInputFormatException(Exception):
    def __init__(self, message='The input format was not recognized.'):
        super().__init__(message)

