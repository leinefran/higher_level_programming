#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{:d} arguments:". format(0))
    elif len(sys.argv) == 2:
        print("{:d} argument:". format(len(sys.argv)-1))
        print("{:d}: {:s}".format(1, sys.argv[1]))
    else:
        print("{:d} arguments:". format(len(sys.argv)-1))
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))
