'''
Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap
years into a list and display the list.
'''

inputYear = int(input("Enter a year: "))
leapYearList = []
for i in range(inputYear + 1, inputYear + 75):
    if i % 4 == 0:
        leapYearList.append(i)
print("The next 15 leap years are")
print(leapYearList[0:15])