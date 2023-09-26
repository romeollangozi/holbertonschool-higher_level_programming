#!/usr/bin/python3
from sys import argv
i = 1
length = len(argv) - 1
if __name__ == "__main__":
    print("{} argument".format(length), end="")
    if length == 0:
        print("s.")
    elif length == 1:
        print(":")
    else:
        print("s:")
    for args in argv[1:]:
        print("{}: {}".format(i, args))
        i += 1
