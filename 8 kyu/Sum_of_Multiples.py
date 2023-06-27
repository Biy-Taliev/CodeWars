'''
Your Job
Find the sum of all multiples of n below m

Keep in Mind
n and m are natural numbers (positive integers)
m is excluded from the multiples
Examples
sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sumMul(4, -7)  ==> "INVALID"

'''

def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"

    n_i = (m - 1) // n
    l_n = n_i * n

    s = n_i * (n + l_n) // 2
    return s