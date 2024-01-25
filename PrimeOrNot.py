'''
Write a Python program to check the given number is prime number or not
'''

number = int(input("Enter number"))
count = 2
temp = 0
while count < number:
    if number % count == 0:
        print("it is not a prime number")
        exit()
        # temp += 1
    count += 1
print("it is a prime number")
# if (temp > 0):
#     print("it is not a prime number")
# else:
#     print("it is a prime number")