import collections
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

    def process(self):
        while True:
            try:
                stack = []
                output = []
                for token in str.split(self.expression):
                    if token.isalnum():
                        output.append(token)
                    elif token in self.funcs:
                        stack.append(stack)
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
            except EOFError:
                break
            except:
                print('error')

        return eval(self.expression)
