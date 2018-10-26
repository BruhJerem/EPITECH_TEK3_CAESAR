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


def xor(b1, b2):
    b = bytearray(len(b1))
    for i in range(len(b1)):
        b[i] = b1[i] ^ b2[i]
    return b


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


def hamming_distance(b1, b2):
    differing_bits = 0
    for byte in xor(b1, b2):
        differing_bits += bin(byte).count("1")
    return differing_bits


def keysize(b):
    normalized_distances = []
    for KEYSIZE in range(5, 41):
        b1 = b[: KEYSIZE]
        b2 = b[KEYSIZE: KEYSIZE * 2]
        b3 = b[KEYSIZE * 2: KEYSIZE * 3]
        b4 = b[KEYSIZE * 3: KEYSIZE * 4]

        normalized_distance = float(
            hamming_distance(b1, b2) +
            hamming_distance(b2, b3) +
            hamming_distance(b3, b4)
        ) / (KEYSIZE * 3)

        normalized_distances.append(
            (KEYSIZE, normalized_distance)
        )

    normalized_distances = sorted(normalized_distances, key=lambda x: x[1])
    return normalized_distances


def break_single_key_xor(b1):
    max_score = 0
    key = None

    for i in range(256):
        b2 = [i] * len(b1)
        plaintext = bytes(xor(b1, b2))
        pscore = score(plaintext)

        if max_score == 0 or pscore > max_score:
            max_score = pscore
            key = bytes([i])

    return key


def main():
    try:
        res = None
        max_score = 0
        if text == '':
            exit(84)
        b = bytearray.fromhex(text)
        normalized_distances = keysize(b)
        for KEYSIZE, _ in normalized_distances[:5]:
            block_bytes = [[] for _ in range(KEYSIZE)]
            for i, byte in enumerate(b):
                block_bytes[i % KEYSIZE].append(byte)

            keys = b""
            for bbytes in block_bytes:
                keys += break_single_key_xor(bbytes)

            key = bytearray(keys * len(b))
            plaintext = bytes(xor(b, key))

            if score(plaintext) > max_score or max_score == 0:
                res = codecs.decode(codecs.encode(keys, 'hex')).upper()[:KEYSIZE]
                max_score = score(plaintext)

        print(res)
    except:
        exit(84)


if __name__ == '__main__':
    main()
