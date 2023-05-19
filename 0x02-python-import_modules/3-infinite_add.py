#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    argc = len(sys.argv)
    i = 0
    sums = 0
    for i in range(1, argc):
        sums = sums + int(sys.argv[i])

    print("{:d}".format(sums))
