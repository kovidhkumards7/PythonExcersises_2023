'''
Write a Python function factorial(num) which returns the factorial of a given number.
'''

number = int(input("Enter a number to find factorial: "))
def factorial(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact
print("Factorial of number " + str(number) + " is " + str(factorial(number)))



'''
Using recursion
'''

numer = int(input("Enter a number to find factorial: "))
def factoria(num):
    if num == 1:
        return 1
    else:
        return (num * factoria(num - 1))

print("Factorial of number " + str(numer) + " is " + str(factoria(numer)))

