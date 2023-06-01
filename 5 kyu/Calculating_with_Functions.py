'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
'''

def zero(operation=None):
    if operation:
        return operation(0)
    return 0

def one(operation=None):
    if operation:
        return operation(1)
    return 1

def two(operation=None):
    if operation:
        return operation(2)
    return 2

def three(operation=None):
    if operation:
        return operation(3)
    return 3

def four(operation=None):
    if operation:
        return operation(4)
    return 4

def five(operation=None):
    if operation:
        return operation(5)
    return 5

def six(operation=None):
    if operation:
        return operation(6)
    return 6

def seven(operation=None):
    if operation:
        return operation(7)
    return 7

def eight(operation=None):
    if operation:
        return operation(8)
    return 8

def nine(operation=None):
    if operation:
        return operation(9)
    return 9

def plus(x):
    return lambda y: y + x

def minus(x):
    return lambda y: y - x

def times(x):
    return lambda y: y * x