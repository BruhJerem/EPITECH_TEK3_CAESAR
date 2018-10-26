#!/usr/bin/env python3

import sys
import codecs
# Check if an argument is giving
if len(sys.argv) != 2:
    print('Error: Invalid argument')
    exit(84)

# Read file
try:
    with open(sys.argv[1]) as file:
        keystr = file.readline().strip('\n')
        text = file.readline().strip('\n')
        if len(text) == 0:
            exit(84)
except IOError:
    print(sys.argv[1], '- does not exist')
    exit(84)
except IndexError:
    print("Please enter input file.")
    exit(84)


def repeating_key_xor(msg, key):
    output_bytes = b''
    index = 0
    for byte in msg:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output_bytes


def main():
    try:
        if text == [''] or keystr == ['']:
            exit(84)
        message = ''.join(text).encode()
        key = ''.join(keystr).encode()
        message = codecs.decode(message, 'hex')
        key = codecs.decode(key, 'hex')
        ciphertext = repeating_key_xor(message, key)
        print(ciphertext.hex().upper())
    except:
        exit(84)

if __name__ == '__main__':
    main()
