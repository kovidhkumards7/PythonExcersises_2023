'''
Write a Python program to find and display the maximum of three given numbers.
'''
number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))
number3 = int(input("Enter third number"))

if not(number1 == number2 and number1 == number3):
    if number1 > number2 and number1 > number3:
        print(str(number1) + " is gretest")
    elif number2 > number3:
        print(str(number2) + " is gretest")
    else:
        print(str(number3) + " is gretest")
else:
    print("All entered numbers are same")
