# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:03:14 2026

@author: darsh
"""
# Program: Ticket Price Calculator

age = int(input("Enter your age: "))

if age <= 5:
    price = "Free"
elif age < 18:
    price = 5
elif age <= 64:
    price = 10
else:
    price = 12

print("Ticket Price:", price)