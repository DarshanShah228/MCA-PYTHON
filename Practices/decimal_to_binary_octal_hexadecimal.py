# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 23:38:09 2026

@author: darsh
"""
# --------------------------------------------------
# Program: Decimal to Binary, Octal and Hexadecimal
# --------------------------------------------------

while True:
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("0. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 0:
        print("Exiting the program...")
        break

    decimal = int(input("Enter a decimal number: "))

    if choice == 1:
        print("Binary Equivalent:", bin(decimal)[2:])

    elif choice == 2:
        print("Octal Equivalent:", oct(decimal)[2:])

    elif choice == 3:
        print("Hexadecimal Equivalent :", hex(decimal)[2:].upper())

    else:
        print("Invalid choice! Please try again.")
