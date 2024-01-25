'''
Write a Python function generate_fibanacci(n) to return a list of first n Fibonacci numbers.
'''

def generate_fibonacci(n):
    a = 0
    b = 1
    fibonacciList = [0,1]
    for i in range(3, n + 1):
        c = a + b
        fibonacciList.append(c)
        a = b
        b = c
    return fibonacciList

number = int(input("Enter the number of terms (should be greater than 2): "))
print(generate_fibonacci(number))