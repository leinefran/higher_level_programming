#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    if new_string is None:
        return (None)
    for i in range(len(new_string)):
        if new_string[i] == 'c' or new_string[i] == 'C':
            del new_string[i]
        return ''.join(new_string)
