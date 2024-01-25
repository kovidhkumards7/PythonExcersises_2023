'''
Write a Python function check_amicable_numbers(num1, num2) that accepts two numbers num1 and num2 as arguments
and returns True if the given pair of numbers are amicable numbers else return false. Invoke the function and
based on return value print the numbers are amicable numbers or not.

num1 and num2 are said to be amicable numbers if sum of all the proper devisors (except num1 itself) of
num1 is equal to num2 and sum of all the proper devisors of num2 (except num1 itself) is equal to num1.

Example: 220 and 284 are amicable numbers as

Proper devisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 whose sum is 284

Proper devisors of 284 are 1, 2, 4, 71, 142 whose sum is 220
'''

print("Checking if two numbers are Amicable numbers or not")
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

sumOfDivisors1 = sumOfDivisors2 = 0

for number in range(1, number1):
    if number1 % number == 0:
        sumOfDivisors1 = sumOfDivisors1 + number

for number in range(1, number2):
    if number2 % number == 0:
        sumOfDivisors2 = sumOfDivisors2 + number

if sumOfDivisors1 == number2 and sumOfDivisors2 == number1:
    print("It is a Amicable number")
else:
    print("It is not a Amicable number")
