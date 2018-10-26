#!/usr/bin/env python3

import sys
import os
import string


def xor(a, b):
    return "".join(["%x" % (int(x, 16) ^ int(y, 16)) for (x, y) in zip(a, b)])


def main():
    if os.path.isfile(sys.argv[1]) == 0:
        exit(84)
    f = open(sys.argv[1], "r")
    lines = f.readlines()
    if len(lines) != 2:
        exit(84)
    lines[0] = lines[0].strip('\n')
    lines[1] = lines[1].strip('\n')
    if len(lines[0]) % 2 != 0 or len(lines[0]) % 2 != 0:
        exit(84)
    if len(lines[0]) == 0 or len(lines[1]) == 0:
        exit(84)
    if len(lines[0]) != len(lines[1]):
        exit(84)
    if all(c in string.hexdigits for c in lines[0]) == 0:
        exit(84)
    if all(c in string.hexdigits for c in lines[1]) == 0:
        exit(84)
    res = xor(lines[0], lines[1])
    print(res.upper())


if __name__ == "__main__":
    main()
