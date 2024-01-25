'''
Write a Python Function is_palindrome(num) that accepts an integer num as argument and returns
True if the num is palindrome else returns false. Invoke the function and based on return value print the output.
'''

number = int(input("Enter a number to find palindrome or not: "))
def is_palindrome(num):
    num1 = num
    temp = 0
    count = 0
    spare = 0
    while num > 0:
        temp = num % 10
        spare = spare * 10 + temp
        num //= 10
    if num1 == spare:
        return True
    else:
        return False
if is_palindrome(number):
    print("It is palindrome")
else:
    print("It is not palindrome")