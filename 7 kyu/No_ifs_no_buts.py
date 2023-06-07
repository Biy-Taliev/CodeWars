'''
Write a function that accepts two numbers a and b and returns whether a is smaller than, bigger than, or equal to b, as a string.

(5, 4)   ---> "5 is greater than 4"
(-4, -7) ---> "-4 is greater than -7"
(2, 2)   ---> "2 is equal to 2"
There is only one problem...

You cannot use if statements, and you cannot use the ternary operator ? :.

In fact the word if and the character ? are not allowed in your code.
'''

def no_ifs_no_buts(a, b):
    small = a < b
    while small:
        return f"{a} is smaller than {b}"
        
    greater = a > b
    while greater:
        return f"{a} is greater than {b}"
    
    equal = a == b
    while equal:
        return f"{a} is equal to {b}"
    
    # OR

    # d = {a<b:'smaller than', a==b:'equal to', a>b: 'greater than'}
    # return f'{a} is {d[True]} {b}'