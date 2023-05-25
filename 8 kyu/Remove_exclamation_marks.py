'''
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
'''

def remove_exclamation_marks(s):
    new_string = []
    for i in s:
        if i != '!':
            new_string.append(i)
    return ''.join(new_string)

#OR 
#   return s.replace('!', '')