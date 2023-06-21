'''
Complete the function that takes a non-negative integer n as input, and returns a 
list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

Examples
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]

'''

def powers_of_two(n):
    power = 0
    lst = [1]
    for i in range(n):
        power += 1
        lst.append(2 ** power)
    return lst