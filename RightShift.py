'''
Write a Python function right_shift(num, n) that takes two numbers num and n as  arguments and returns
value of the integer num rotated to the right by n positions. Assume both the numbers are unsigned.
Invoke the function and print the return value.

Hint: use >> binary operator to shift the bits.

Example: num=60, n=2 result=15
'''

def right_shift(num, n):
    binNumber = bin(num)
    binNumber = str(binNumber)
    binNumber = binNumber[2:]
    print(binNumber)
    temp = ""
    temp = binNumber[-1:n+1:-1]
    print(temp)
    # temp = temp[::-1]
    temp = temp + binNumber[0:len(binNumber) - n]
    print(temp)
    return (int(temp,2))

number = int(input("Enter a number: "))
shift = int(input("Enter shift value: "))
print(right_shift(number, shift))

#Alternate way
def rs(num,n):
    return num>>n

# Driver Program
print(rs(60,2))