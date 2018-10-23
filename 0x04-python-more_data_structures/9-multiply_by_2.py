#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return (a_dictionary.update((k, v * 2) for k, v in a_dictionary.items()))
