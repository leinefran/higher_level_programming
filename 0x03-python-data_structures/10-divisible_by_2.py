#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for num in range(len(my_list)):
        if num % 2 == 0:
           new_list =  new_list.append(True)
        else:
            new_list = new_list.append(False)
    return new_list
