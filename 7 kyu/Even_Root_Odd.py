'''
Complete the function that takes a list of numbers (), as the only argument to the function. 
Take each number in the list and square it if it is even, or square root the number if it is odd. 
Take this new list and return the sum of it, rounded to two decimal places.nums

The list will never be empty and will only contain values that are greater than or equal to zero.

Good luck!
'''
import math
def sum_square_even_root_odd(nums):
    modified_nums = []

    for num in nums:
        if num % 2 == 0:
            modified_nums.append(num ** 2)
        else:
            modified_nums.append(math.sqrt(num))

    return round(sum(modified_nums), 2)