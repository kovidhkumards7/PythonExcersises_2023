'''
Write a Python function, find_square() that accepts an integer number n and
returns the square of n. Invoke the function and display the square of the number.
'''

number = int(input("Enter a number to find square of: "))
def squareOfNumber(num):
    return num**2
print("Square of " + str(number) + " is " + str(squareOfNumber(number)))