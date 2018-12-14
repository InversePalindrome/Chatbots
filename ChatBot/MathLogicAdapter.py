import cexprtk 

from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement


class MathLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    def can_process(self, statement):
        return True

    def process(self, statement):
        solution = Statement(str(cexprtk.evaluate_expression(statement.text, {})))
        solution.confidence = 1
        
        return solution
