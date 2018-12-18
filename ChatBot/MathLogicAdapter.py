"""
Copyright (c) 2018 Inverse Palindrome
Chatbot - MathLogicAdapter.py
https://inversepalindrome.com/
"""


import ast
import Slack
import cexprtk 
import numpy as np
import matplotlib.pyplot as plt

from pynumparser import NumberSequence
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement


symbol_table = cexprtk.Symbol_Table({}, {}, True)
sequence_parser = NumberSequence(float)

def evaluate_expression(expression):
    try:
        evaluated_expression = cexprtk.Expression(expression, symbol_table)()
    except cexprtk.ParseException:
        return Statement("Expression couldn't be evaluated!")
           
    if evaluated_expression.is_integer():
        evaluated_expression = int(evaluated_expression)
        
    return Statement(str(evaluated_expression))

def import_symbols(expression):
    symbols = expression.split(' ', 1)
    symbol_type = symbols[0]
    symbols_dict = symbols[1].strip()

    try:
        if symbol_type == "constants":
            symbol_table._populateConstants(ast.literal_eval(symbols_dict), True)
            return Statement("Constants imported.")
        elif symbol_type == "variables":
            symbol_table._populateVariables(ast.literal_eval(symbols_dict))
            return Statement("Variables imported.")
    except (SyntaxError, ValueError):
        return Statement("Nothing could be imported.")    

def plot_function(expression):
    expression_list = expression.split(',', 1)

    equation_string = expression_list[0].strip()
    range_string = expression_list[1].strip()
   
    x = np.array(sequence_parser(range_string))
    y = eval(equation_string)
  
    plt.plot(x, y)
    plt.savefig("plot.png")

    Slack.filename = "plot.png"

    return Statement("Equation " + equation_string + " graphed.")

class MathLogicAdapter(LogicAdapter):
    def can_process(self, statement):
        return (statement.text.startswith("Evaluate") and len(statement.text.split(' ', 1)) > 1) or (
            statement.text.startswith("Import") and len(statement.text.split(' ', 2)) > 2) or (
                statement.text.startswith("Plot") and len(statement.text.split(',', 1)) > 1) 

    def process(self, statement):
        statement_text = statement.text.split(' ', 1)
      
        command = statement_text[0]
        expression = statement_text[1]

        if command == "Evaluate":
            return evaluate_expression(expression)
        elif command == "Import":
            return import_symbols(expression)
        elif command == "Plot":
            return plot_function(expression)
        else:
            return Statement("Can't comprehend expression")