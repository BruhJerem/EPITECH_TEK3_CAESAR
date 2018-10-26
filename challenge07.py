#!/usr/bin/env python3

import sys
import base64
from Crypto.Cipher import AES

# Check if an argument is giving
if len(sys.argv) != 2:
    print('Error: Invalid argument')
    exit(84)

# Read file
try:
    with open(sys.argv[1]) as file:
        keystr = file.readline().strip('\n')
        text = file.readline()
        if len(keystr) % 16 != 0:
            exit(84)
        if len(text) == 0:
            exit(84)
except IOError:
    print(sys.argv[1], '- does not exist')
    exit(84)


def hex_decode(msg):
    if type(msg) == bytes:
        msg = msg.decode()
    return bytes.fromhex(msg)


def base64_encode(msg):
    if type(msg) == str:
        msg = msg.encode()
    return base64.b64encode(msg)


def base64_decode(msg):
    if type(msg) == str:
        msg = msg.encode()
    return base64.b64decode(msg)


def unpad(plaintext):
    return plaintext[:-ord(plaintext[len(plaintext) - 1:])]


def decrypt_aes_ecb(msg, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(msg))


def main():
    message = base64_decode(''.join(text).encode())
    key = hex_decode(''.join(keystr).encode())
    ciphertext = decrypt_aes_ecb(message, key)
    print(base64_encode(ciphertext).decode('utf-8'))


if __name__ == '__main__':
    main()
