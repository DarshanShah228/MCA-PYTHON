# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:07:24 2026

@author: darsh
"""

# Program: Star Triangle Pattern

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("* ", end=" ")
    print()