# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:26:55 2026

@author: darsh
"""
# Program: Maximum Using Lambda Function

maximum = lambda first, second: first if first > second else second
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print("Maximum =", maximum(first, second))