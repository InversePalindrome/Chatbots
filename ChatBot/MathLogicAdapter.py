import ast
import cexprtk 

from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement


symbol_table = cexprtk.Symbol_Table({}, {}, True)

def evaluate_expression(expression):
    try:
        evaluated_expression = cexprtk.Expression(expression, symbol_table)()
    except cexprtk.ParseException:
        return Statement("Expression couldn't be evaluated!")
            
    solution = Statement(str(evaluated_expression))
    solution.confidence = 1
        
    return solution

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

class MathLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    def can_process(self, statement):
        return (statement.text.startswith("Evaluate") and len(statement.text.split(' ', 1)) > 1) or (
            statement.text.startswith("Import") and len(statement.text.split(' ', 2)) > 2)

    def process(self, statement):
        statement_text = statement.text.split(' ', 1)

        command = statement_text[0]
        expression = statement_text[1]

        if command == "Evaluate":
            return evaluate_expression(expression)
        elif command == "Import":
            return import_symbols(expression)
        else:
            return Statement("Can't comprehend expression")