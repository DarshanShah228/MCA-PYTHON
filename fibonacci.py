# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:05:17 2026

@author: darsh
"""

# Program: Fibonacci Series

def fibonacci(limit):
    a, b = 0, 1

    while a < limit:
        print(a, end=" ")
        a, b = b, a + b

limit = int(input("Enter the limit: "))
fibonacci(limit)