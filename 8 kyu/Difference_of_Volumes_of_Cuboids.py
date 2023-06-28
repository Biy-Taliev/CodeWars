'''
In this simple exercise, you will create a program that will take two lists of integers, and . 
Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids and . 
You must find the difference of the cuboids' volumes regardless of which is bigger.abab

For example, if the parameters passed are , the volume of is 12 and the volume of is 20. 
Therefore, the function should return 8.([2, 2, 3], [5, 4, 1])ab

Your function will be tested with pre-made examples as well as random ones.

If you can, try writing it in one line of code.

'''

def find_difference(a, b):
    mult_1 = 1
    mult_2 = 1
    for i,j in zip(a,b):
        mult_1 *= i
        mult_2 *= j
        
    return mult_1 - mult_2 if mult_1 > mult_2 else mult_2 - mult_1