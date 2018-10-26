#!/usr/bin/env python


import sys
import codecs
from collections import defaultdict

# Read file
try:
    with open(sys.argv[1]) as file:
        text = file.read()
except IOError:
    print(sys.argv[1], '- does not exist')
    exit(84)
except IndexError:
    print("Please enter input file.")
    exit(84)


def repeated_blocks(buffer, block_length):
    reps = defaultdict(lambda: -1)
    for i in range(0, len(buffer), block_length):
        block = bytes(buffer[i:i + block_length])
        reps[block] += 1
    return sum(reps.values())


def main():
    try:
        if text == '':
            exit(84)
        max_reps, tmp, res = 0, 0, 0
        block_length = 16
        content = text.split('\n')
        for ciphertext in content:
            ciphertext = codecs.decode(ciphertext, 'base64')
            ciphertext = ciphertext.rstrip()
            reps = repeated_blocks(bytearray(ciphertext), block_length)
            tmp += 1
            if reps > max_reps:
                max_reps = reps
                res = tmp

        print(res)
    except:
        exit(84)


if __name__ == '__main__':
    main()
