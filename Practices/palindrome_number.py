# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 00:42:06 2026

@author: darsh
"""
'''
without suing slicing find palindrome number
'''
n = 121
temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if n == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")