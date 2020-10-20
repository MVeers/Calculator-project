class Calculate:
    expression = ""
    answer = ""

    def __init__(self, expression):
        self.expression = expression

    def process(self):
        answer = eval(self.expression)
        return eval(self.expression)
