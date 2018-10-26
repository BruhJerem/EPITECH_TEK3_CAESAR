#!/usr/bin/env python3

import sys
import os
import string
import codecs


def xor(b1, b2):
    b = bytearray(len(b1))
    for i in range(len(b1)):
        b[i] = b1[i] ^ b2[i]
    return b


# score byte
def score(s):
    freq = {}
    freq[' '] = 700000000
    freq['e'] = 390395169
    freq['t'] = 282039486
    freq['a'] = 248362256
    freq['o'] = 235661502
    freq['i'] = 214822972
    freq['n'] = 214319386
    freq['s'] = 196844692
    freq['h'] = 193607737
    freq['r'] = 184990759
    freq['d'] = 134044565
    freq['l'] = 125951672
    freq['u'] = 88219598
    freq['c'] = 79962026
    freq['m'] = 79502870
    freq['f'] = 72967175
    freq['w'] = 69069021
    freq['g'] = 61549736
    freq['y'] = 59010696
    freq['p'] = 55746578
    freq['b'] = 47673928
    freq['v'] = 30476191
    freq['k'] = 22969448
    freq['x'] = 5574077
    freq['j'] = 4507165
    freq['q'] = 3649838
    freq['z'] = 2456495
    score = 0
    for c in s.lower():
        for j in freq:
            if chr(c) == j:
                score += freq[j]
    return score


def main():
    if len(sys.argv) != 2:
        print("No input file.")
        exit(84)
    if os.path.isfile(sys.argv[1]) == 0:
        print("File not exist.")
        exit(84)

    f = open(sys.argv[1], "r")
    content = f.read().split('\n')
    if content == ['']:
        exit(84)
    # bruteforce
    try:
        index = 0
        max_score = 0
        key = None
        for c in content:
            try:
                if all(p in string.hexdigits for p in c) == 0:
                    exit(84)
                b1 = bytearray.fromhex(c)
                for i in range(0, 256):
                    b2 = [i] * len(b1)
                    plaintext = bytes(xor(b1, b2))
                    pscore = score(plaintext)

                    if max_score == 0 or pscore > max_score:
                        maxi = index
                        english = plaintext
                        max_score = pscore
                        key = bytes([i])
                index += 1
            except:
                exit(84)

        print(codecs.decode(codecs.encode(key, 'hex'), 'utf-8').upper() + " " + str(maxi))
    except:
        exit(84)


if __name__ == "__main__":
    main()
