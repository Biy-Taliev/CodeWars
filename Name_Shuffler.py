'''
Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john"
'''

def name_shuffler(str_):
    return ' '.join((str_.split()) [::-1]) 
    #  return ' '.join(reversed(s.split()))