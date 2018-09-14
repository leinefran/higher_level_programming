#!/usr/bin/python3
for n in range(0, 8): #n stands for numbers
    for n2 in range(1, 10):
        if n2 > n:
            print("{:d}{:d}, ".format(n, n2), end="")
print("{:d}".format(89))
