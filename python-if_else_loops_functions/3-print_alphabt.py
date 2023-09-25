#!/usr/bin/python3
a = 97
while a < 123:
    if a != 113 and a != 101:
        print("{}".format(chr(a)), end="")
    a += 1
