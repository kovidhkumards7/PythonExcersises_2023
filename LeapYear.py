'''
Write a Python program to check whether the given year is leap year or not.
'''

year = int(input("Enter year : "))
if year % 4 == 0:
    print("it is a leap year")
else:
    print("it is not a leap year")