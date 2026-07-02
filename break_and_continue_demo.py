# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:17:23 2026

@author: darsh
"""
# Program: Break and Continue

print("Display Numbers from 0 to 9\n")

for number in range(10):

    if number == 3:
        print("Continue")
        continue

    if number == 7:
        print("Break")
        break

    print(number)