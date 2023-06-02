'''
Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.

Example:
For input: [3, 4, 4, 3, 6, 3]

remove the at index 30
remove the at index 41
remove the at index 33
Expected output: [4, 6, 3]

More examples can be found in the test cases.

Good luck!
'''

def solve(arr):
    
    new = []
    for i in arr:
        if i not in new:
            new.append(i)
        else:
            new.remove(i)
            new.append(i)
    return new