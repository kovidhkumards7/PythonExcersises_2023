'''
Write a Python program that displays a message as follows for a given number:

If it is a multiple of 3, display "Zip"

If it is a multiple of 5, display "Zap"

If it is a multiple of both 3 and 5, display "Zoom"

If it does not satisfy any of the above given conditions, display "Invalid"
'''

number = int(input("Enter a number: "))
if (number % 3 == 0 and number % 5 == 0):
    print("Zoom")
elif (number % 3 == 0):
    print("Zip")
elif (number % 5 == 0):
    print("Zap")
else:
    print("Invalid")



