#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if ld > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".
          format(number, ld))
if ld == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, ld))
if ld < 6 and ld != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".
          format(number, ld))
