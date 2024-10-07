# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
num = input("Write an integer 4-digit number:")

if num.isdigit() and int(num)//10**3>0:
    num_int = int(num)
    sum_num = int(num_int//10**3+ num_int//10**2%10 + num_int//10%10 + num_int%10)
    print(num_int//10**3,num_int//10**2%10,num_int//10%10,num_int%10, sum_num)
else:
    print("Incorrect input")