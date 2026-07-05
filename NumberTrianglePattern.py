# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:01:19 2026

@author: darsh
"""
# Program: Number Triangle Pattern


def number_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

rows = int(input("Enter the number of rows: "))
number_triangle(rows)