# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:24:25 2026

@author: darsh
"""
# Program: Even or Odd Using Lambda Function

check = lambda number: "Even" if number % 2 == 0 else "Odd"
number = int(input("Enter a number: "))
print("Number is", check(number))