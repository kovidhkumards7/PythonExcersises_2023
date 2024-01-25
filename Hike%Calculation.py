'''
An organization has decided to provide salary hike to its employees based on their job level.
Employees can be in job levels 3 , 4 or 5. Hike percentage based on job levels are given below:

Job level   Hike Percentage (applicable on current salary)
3           15
4           7
5           5

In case of invalid job level, consider hike percentage to be 0.

Given the current salary and job level, write a Python program to find and display the new salary of an employee.
'''

salary = float(input("Enter your salary: "))
jobLevel = int(input("Enter your job level: "))
hikePercentage = 0
if (jobLevel == 3):
    hikePercentage = 15
elif (jobLevel == 4):
    hikePercentage = 7
elif (jobLevel == 5):
    hikePercentage = 5
salary = salary + salary * hikePercentage / 100
print("Your salary after hike is " + str(salary))
