#!/usr/bin/python3
a = 0
while a < 100:
    if a != 99:
        print("{:02d}, ".format(a), end="")
    else:
        print("{}".format(a))
    a += 1
