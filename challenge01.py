#!/usr/bin/env python3

import codecs
import os
import string
import sys


def main():
    # Check if an argument is giving
    if len(sys.argv) != 2:
        print('Error: Invalid argument')
        exit(84)

    if os.path.isfile(sys.argv[1]) == 0:
        exit(84)
    f = open(sys.argv[1], "r")
    content = f.read()
    if content == "":
        exit(84)
    content = content.replace('\n', '')
    if all(c in string.hexdigits for c in content) == 0:
        exit(84)
    j = len(content) % 2
    if j != 0:
        exit(84)
    encoded = codecs.decode(content, 'hex')
    encoded = codecs.encode(encoded, 'base64')
    encoded = codecs.decode(encoded)
    encoded = encoded.replace('\n', '')
    print(encoded)


if __name__ == "__main__":
    main()
