#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    old_list = my_list[:]
    old_list[idx] = element
    return (old_list)
