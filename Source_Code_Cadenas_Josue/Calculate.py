import math


def pop(stack):
    return stack.pop()


def isEmpty(stack):
    if not stack:
        return True
    else:
        return False


def peek(stack):
    if isEmpty(stack):
        return 1
    else:
        return stack[len(stack) - 1]


# a > b?
def precendence(self, a):
    if a.isalnum():
        return -1
    if a in self.ops:
        if a == '^':
            return 3
        elif a == '*' or '/' or '%':
            return 2
        else:  # a == + or -
            return 1
    else:  # is a function (
        return 0


def association(self, a):
    if a.isalnum():
        return "none"
    if a in self.ops and a != '^':
        return "left"
    else:  # is a function or ^
        return "right"


class Calculate:
    expression = ""
    ops = {'+',
           '-',
           '*',
           '/',
           '^',
           '('
           ')'
           }
    funcs = {
        'sin', 'cos', 'tan', 'cot'
    }

    def __init__(self, expression):
        self.expression = expression

    # operator functions
    def add(self, a, b):
        c = float(a) + float(b)
        return c

    def sub(self, a, b):
        c = float(b) - float(a)
        return c

    def sub1(self, a):
        return float(-a)

    def mult(self, a, b):
        c = float(a) * float(b)
        return c

    def divide(self, a, b):
        if a == '0':
            return "error"
        else:
            c = float(b) / float(a)
            return c

    def power(self, a, b):
        c = float(a) ** float(b)
        return c

    def sin(self, a):
        c = math.sin(float(a))
        return c

    def cos(self, a):
        c = math.cos(float(a))
        return c

    def tan(self, a):
        c = math.tan(float(a))
        return c

    # processing
    def outProcess(self, output):
        try:
            total = 0
            stack = []
            num1 = 0
            num2 = 0
            for token in output:
                if token.isalnum() and token not in self.funcs:
                    stack.append(token)
                elif token in self.ops and peek(stack) in self.ops:
                    return "error"
                elif token == '-' and len(stack) == 1:
                    num1 = pop(stack)
                    total = self.sub1(num1)
                    stack.append(total)
                elif token == '-':
                    num1 = pop(stack)
                    num2 = pop(stack)
                    total = self.sub(num1, num2)
                    stack.append(total)
                elif token == '+':
                    num1 = pop(stack)
                    num2 = pop(stack)
                    total = self.add(num1, num2)
                    stack.append(total)
                elif token == '*':
                    num1 = pop(stack)
                    num2 = pop(stack)
                    total = self.mult(num1, num2)
                    stack.append(total)
                elif token == '/':
                    num1 = pop(stack)
                    num2 = pop(stack)
                    total = self.divide(num1, num2)
                    stack.append(total)
                elif token == '^':
                    num1 = pop(stack)
                    num2 = pop(stack)
                    total = self.power(num1, num2)
                    stack.append(total)
                elif token == 'sin':
                    num1 = pop(stack)
                    total = self.sin(num1)
                    stack.append(total)
                elif token == 'cos':
                    num1 = pop(stack)
                    total = self.cos(num1)
                    stack.append(total)
                elif token == 'tan':
                    num1 = pop(stack)
                    total = self.tan(num1)
                    stack.append(total)
            return total
        except:
            return "error"

    # main shunting yard algorithm

    def process(self):
        total = 0
        while True:
            try:
                stack = []
                output = []
                for token in str.split(self.expression):
                    if token in self.funcs:
                        stack.append(token)
                    elif token.isalnum():
                        output.append(token)
                    elif token in self.ops:
                        while (peek(stack) in self.ops and
                               precendence(self, peek(stack)) > precendence(self, token) or
                               peek(stack) in self.ops and
                               precendence(self, token) == precendence(self, peek(stack)) and
                               association(self, token) == "left") and token != '(':
                            output.append(pop(stack))
                        stack.append(token)
                    elif token == '(':
                        stack.append(token)
                    elif token == ')':
                        while peek(stack) != '(' and not isEmpty(stack):
                            output.append(pop(stack))
                            if peek(stack) == '(':
                                trash = pop(stack)
                while not isEmpty(stack):
                    output.append(pop(stack))
                print output
                total = self.outProcess(output)
                print total
                break
            except EOFError:
                break
            except:
                print('error')
                break
        return total
