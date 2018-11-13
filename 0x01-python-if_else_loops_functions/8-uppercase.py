#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for char in str:
        # check if char is lowercase
        if ord(char) > 96 and ord(char) < 123:
            # convert lower case to upper case; ASCII value
            char = chr(ord(char) - 32)
            upper_str += char
        else:
            upper_str += char
    print("{:s}".format(upper_str))
