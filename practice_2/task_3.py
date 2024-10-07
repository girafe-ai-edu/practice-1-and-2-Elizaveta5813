# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
weight = input()
height = input()

if (weight.isdigit() * height.isdigit() == 0) or (int(weight)*int(height)==0):
    print("Incorrect inputs. Try again with numeric positive data")
else:
    BMI = int(weight) / int(height)**2
    print(BMI)
