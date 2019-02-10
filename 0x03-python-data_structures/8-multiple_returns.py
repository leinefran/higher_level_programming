#!/usr/bin/python3
def multiple_returns(sentence):

    new_tuple = ()

    if not sentence or if len(sentence) == 0:
        new_tuple = 'None'
    else:
        new_tuple = len(sentence), sentence[0]

    return new_tuple
