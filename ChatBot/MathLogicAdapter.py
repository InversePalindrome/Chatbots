import ast
import cexprtk 

from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement


class MathLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    def can_process(self, statement):
        return len(statement.text) > 0

    def process(self, statement):
        formula = statement.text.split(",", 1)
        
        expression = formula[0]
        symbol_table = {}

        if len(formula) > 1:
            try:
                symbol_table = ast.literal_eval(formula[1].strip())
            except(ValueError, SyntaxError):
                return Statement("Symbol-Table couldn't be parsed!")

        try:
            evaluaded_expression = cexprtk.evaluate_expression(expression, symbol_table)
        except cexprtk.ParseException:
            return Statement("Expression couldn't be evaluated!")
            
        solution = Statement(str(evaluaded_expression))
        solution.confidence = 1
        
        return solution
