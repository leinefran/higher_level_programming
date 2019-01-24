#!/usr/bin/python3
'''Module find_peak'''


def find_peak(list_of_integers):
    '''A function that finds a peak in a list of unsorted integers'''

    if list_of_integers:
        # first, sort the list:
        list_of_integers.sort()

        # return last element, which is the max:
        return(list_of_integers[-1])

    return(None)
