# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 00:34:45 2026

@author: darsh
"""
'''
read a paragraph in world file and find the frequency on each word using dictionary
'''

file = open("E:\MCA\Training Workshop\Python\Practices\paragraph.txt", "r")
text = file.read().lower().split()
freq = {}

for word in text:
    freq[word] = freq.get(word, 0) + 1

for word in freq:
    print(word, ":", freq[word])

file.close()