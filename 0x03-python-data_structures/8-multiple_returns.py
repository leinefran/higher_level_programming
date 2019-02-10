#!/usr/bin/python3
def multiple_returns(sentence):

    new_tuple = ()

    if not sentence:
        new_tuple = 'None'
    elif len(sentence) == 0:
        new_tuple = (0, sentence[0])
    else:
        new_tuple = len(sentence), sentence[0]

    return new_tuple
