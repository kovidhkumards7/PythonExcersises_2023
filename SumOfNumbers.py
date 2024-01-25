'''
Write a Python function, find_sum() that accepts an integer n and
returns the sum of first n numbers. Invoke the function and display the sum of first n numbers.
'''

number = int(input("Enter a number to find sum: "))
def sumOfNumber(num):
    count = 0
    sumOfN = 0
    while count <= num:
        sumOfN += count
        count += 1
    return sumOfN
print("Square of " + str(number) + " is " + str(sumOfNumber(number)))