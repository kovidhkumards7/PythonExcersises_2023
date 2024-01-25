'''
Write a Python program to find the reverse of digits of a given number.

Example: reverse of digits of the number 123 will be 321

Note: Initialize the number with various values and test your program.
'''



number = int(input("Enter a number: "))
count = number
reverse = ""
while number > 0:
    temp = number % 10
    reverse = reverse + (str(temp))
    number //= 10
print("Reverse of " + str(count) + " is : " + reverse)
