#!/usr/bin/env python3

import base64

enc_pass = "YTE2Yjc5MDA0MmQxMmYyNg==" # encrypted flag
enc_pass = base64.b64decode(enc_pass).decode() # base64 decode
enc_pass = int(enc_pass, 16) 
enc_pass ^= 0xABCDEFFEDCBAABC # XOR with the constant

# .log file contains the XORed values from the loop in the encryption
logs = [] # List to store the XORed values from .log file
with open(".log", 'r') as f:
    for line in f:
        line = line.split(" ")
        logs.append(int(line[3]))

# Depcrytion must happen in the reverse order
logs.reverse()

logs.insert(0, enc_pass)

# XOR: "a ^ b = c" then "b ^ c = a" and "a ^ c = b"
# Using the above properties of XOR decrypt the flag
def decrypt():
    c = int('101010101A5', 16) 
    const_b = 0xABD79CC494212625
    rev_pass = ''
    for i in range(len(logs) - 2):
       char = int((logs[i] ^ logs[i+1]) / c)
       rev_pass += chr(char)
    b = int((const_b ^ logs[-2]) / c)
    rev_pass += chr(b)
    return rev_pass[::-1]

print(decrypt())
