'''
Write a Python program to find the sum of digits of a given number.

Example: Sum of digits of the number 123 will be 6

Note: Initialize the number with various values and test your program.
'''


number = int(input("Enter a number: "))
sum = temp = 0
temp = count = number
while number > 0:
    temp = number % 10
    sum += temp
    number //= 10
print("The sum of the given number " + str(count) + " is : " + str(sum))