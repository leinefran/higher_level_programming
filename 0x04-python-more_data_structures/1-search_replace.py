#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def func(number):
        if number is search:
            number = replace
        return number
    new_list = []
    new_list = list(map(lambda number: func(number), my_list))
    return new_list
