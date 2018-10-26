#!/usr/bin/env python3

import sys
import codecs

# Read file
try:
    with open(sys.argv[1]) as file:
        text = file.readline().strip('\n')
except IOError:
    print(sys.argv[1], '- does not exist')
    exit(84)
except IndexError:
    print("Please enter input file.")
    exit(84)


def main():
    if text == '':
        exit(84)


if __name__ == '__main__':
    main()
