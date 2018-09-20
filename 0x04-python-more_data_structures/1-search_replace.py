#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def func(n):
       return (replace if n is search else n)
    new_list = []
    new_list = list(map(lambda n: func(n), my_list))
    return new_list
