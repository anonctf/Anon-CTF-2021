#!/usr/bin/env python3

import base64

m = ['0x73', '0x31', '0x4e', '0x47', '0x5f']

"""
    anonCTF{S4mPl3_F14g_f0rm47}
"""

base = b'YW5vbkNURns='

nu = [22, 21, 33, 21, 22]

def main():
    j = ['0b1111101', '0b1111001', '0b110101', '0b110100', '0b1000101', '0b1011111', '0b110101', '0b110001']

    my_dict = {
        0: 'q', 1: 'e', 2: '5', 3: 't',
        4: 'u', 5: '4', 6: 'o', 7: 'a',
        8: '7', 9: 'd', 10: 'g', 11: '8',
        12: 'j', 13: 'l', 14: '6', 15: '9',
        16: 'z', 17: 'c', 18: 'b', 19: 'm',
        20: 'w', 21: '3', 22: 'r', 23: 'y',
        24: '1', 25: 'i', 26: 'p', 27: 's',
        28: 'f', 29: 'h', 30: 'k', 31: 'x',
        32: '2', 33: 'v', 34: 'n'
    }

    print("\n")
    print("\t\tPassword Checker\n")
    password = input("Enter the Password: ")
    if len(password) == 26:
        if fun1(password[13:18]) and fun2(password[18:], j) and fun3(password[8:13], my_dict) and fun4(password[:8]):
            print("You cracked it!!\n")
        else:
            print("Try Harder.\n")
    else:
        print("Incorrect\n")

def fun1(a):
    l1 = []
    
    for i in list(a):
        l1.append(hex(ord(i))) 

    if l1 == m:
        return True
    return False

def fun2(b, k):
    l2 = []

    for i in list(b):
        l2.append(bin(ord(i)))

    k.reverse()
    if l2 == k:
        return True
    return False

def fun3(c, your_dict):
    s1 = ''

    for i in nu:
        s1 += your_dict[i]

    if s1 == c:
        return True
    return False

def fun4(d):
    s2 = base64.b64encode(bytes(d, "utf-8"))

    if s2 == base:
        return True
    return False

main()