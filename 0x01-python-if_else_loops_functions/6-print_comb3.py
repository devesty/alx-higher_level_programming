#!/usr/bin/python3
for digit1 in range(0, 10):
    for digitb in range(digit1 + 1, 10):
        if digit1 == 8 == digitb == 9:
            print("{}{}".format(digit1, digitb))
        else:
            print("{}{}".format(digit1, digitb), end=", ")
