#!/usr/bin/python3
'''Module find_peak'''


def find_peak(list_of_integers):
    '''A function that finds a peak in a list of unsorted integers'''

    if list_of_integers:
        peak = max(list_of_integers)
        return(peak)
    return(None)
