#!/usr/bin/python3
from sys import argv
i = 1
length = len(argv) - 1
if __name__ == "__main__":
    print("{} arguments".format(length), end="")
    if length == 0:
        print(".")
    else:
        print(":")
    for args in argv[1:]:
        print("{}: {}".format(i, args))
        i += 1
