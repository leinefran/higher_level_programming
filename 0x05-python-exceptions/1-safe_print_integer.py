#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except:
        pass
        print("{} is not an interger".format(value))
        return False
