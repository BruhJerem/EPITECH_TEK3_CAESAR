#!/usr/bin/env python3


import sys
import codecs
from Crypto.Cipher import AES

# Read file
try:
    with open(sys.argv[1]) as file:
        keytext = file.readline().strip('\n')
        ivtext = file.readline().strip('\n')
        text = file.readline().strip('\n')
except IOError:
    print(sys.argv[1], '- does not exist')
    exit(84)
except IndexError:
    print("Please enter input file.")
    exit(84)


def aes_128_ecb_dec(buffer, key):
    obj = AES.new(key, AES.MODE_ECB)
    j = len(buffer) % AES.block_size
    if j != 0:
        for i in range(j, AES.block_size):
            buffer += bytes([0])
    return bytearray(obj.decrypt(bytes(buffer)))


# faire xor entre deux strings
def xor(b1, b2):
    b = bytearray(len(b1))
    for i in range(len(b1)):
        b[i] = b1[i] ^ b2[i]
    return b


def aes_128_cbc_dec(ciphertext, key, iv):
    plaintext = bytearray(len(ciphertext))
    prev_block = iv
    for i in range(0, len(ciphertext), AES.block_size):
        if i == 0:
            plaintext[i: i + AES.block_size] = aes_128_ecb_dec(bytes(ciphertext[i: i + AES.block_size]), key)
        else:
            plaintext[i: i + AES.block_size] = xor(
                aes_128_ecb_dec(bytes(ciphertext[i: i + AES.block_size]), key),
                prev_block
            )
        prev_block = ciphertext[i: i + AES.block_size]
    return codecs.encode(plaintext, 'base64')


def main():
    try:
        if text == '' or ivtext == '' or keytext == '':
            exit(84)
        plaintext = codecs.encode(text)
        plaintext = codecs.decode(plaintext, 'base64')
        plaintext = bytearray(plaintext)
        iv = codecs.decode(ivtext, 'hex')
        iv = bytearray(bytes(iv))
        key = codecs.decode(keytext, 'hex')
        plaintext = codecs.decode(aes_128_cbc_dec(plaintext, key, iv))
        plaintext = plaintext.replace('\n', '')
        print(plaintext)
    except:
        exit(84)


if __name__ == '__main__':
    main()
