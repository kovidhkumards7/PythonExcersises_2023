'''
Write a Python function check_strong_number(num) that accepts a positive integer as argument and
returns True if the number is strong number else false. Invoke the function and based on return
value print the number is strong number or not.

A number is said to be strong number, if the sum of factorial of each digit of the
number is equal to the given number.

Example:145 is strong number as

1!=1

4!=24

5!=120

Sum of all these is 145
'''

import math

number = int(input("Enter a number to find it's amstrong or not: "))

def check_strong_number(num):
    sumOfFactorialOfDigits = 0
    number1 = num
    temp = count = 0

    while num > 0:
        temp = num % 10
        sumOfFactorialOfDigits += math.factorial(temp)
        num //= 10

    if (number1 == sumOfFactorialOfDigits):
        return True
    else:
        return False

if check_strong_number(number):
    print("It is a Amstrong number")
else:
    print("It is not a Amstrong number")

