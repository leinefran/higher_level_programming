#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    def func(value):
        return (value in my_list * number)
    new_list = list(map(lambda n: func(n), my_list))
    return new_list
