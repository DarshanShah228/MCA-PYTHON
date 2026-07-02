# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:26:24 2026

@author: darsh
"""
# Program: Celsius to Fahrenheit

convert = lambda celsius: (celsius * 9 / 5) + 32
temperature = float(input("Enter temperature in Celsius: "))
print("Fahrenheit =", convert(temperature))