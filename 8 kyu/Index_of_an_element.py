'''
Provided is a function which accepts two parameters in the following order: and s the index of the element if found and otherwise. 
Your task is to shorten the code as much as possible in order to meet the 
strict character count requirements of the Kata. (no more than 161) You may assume that all array elements are unique.Kataarray, elementreturn"Not found"
'''

def find(a, el):
    return a.index(el) if el in a else 'Not found'