'''
Write a Python function proper_divisors(num) which returns a list of all the proper divisors of given number.

Example: Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
'''

def proper_divisor(num):
    listOfProperDivisors = []
    for numb in range(1, num):
        if num % numb == 0:
            listOfProperDivisors.append(numb)
    return listOfProperDivisors

number = int(input("Enter a number: "))
print(proper_divisor(number))