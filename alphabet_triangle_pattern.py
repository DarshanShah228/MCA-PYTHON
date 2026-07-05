# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:08:27 2026

@author: darsh
"""

# Program: Alphabet Triangle Pattern

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    ch = 65  # ASCII value of 'A'

    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1

    print()