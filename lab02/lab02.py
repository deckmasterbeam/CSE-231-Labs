# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:06:37 2016

@author: joshuabarnett
"""

input_str = input("Input an interger (0 terminates): ")
input_int = int(input_str)

odd_sum = 0
odd_count = 0
even_sum = 0
even_count = 0
total_positive = 0

while input_int != 0 :
    if input_int < 0:
        print("Hey silly, dats wrong.")
    elif input_int % 2 != 0:
        odd_sum += input_int
        odd_count += 1
    elif input_int%2 == 0:
        even_sum += input_int
        even_count += 1
    if input_int > 0 :
        total_positive += 1
    input_str = input("Input an interger (0 terminates): ")
    input_int = int(input_str)
    
print("sum of odds: ", odd_sum)
print("sum of evens: ", even_sum)
print("odd count: ", odd_count)
print("even_count: ", even_count)
print("total positive integer count: ", total_positive)