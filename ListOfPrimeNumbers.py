'''
Given a list of numbers, write a Python function to return the list of prime numbers present in it.

Example: input:[7,9,11,13,15,20,23]
         output:[7,11,13,23]
'''

size = int(input("Enter the number of numeric elements in a list: "))
inputList = []
primeList = []

for i in range(0, size):
    inputList.append(int(input("Enter list element: ")))
print(inputList)

for i in inputList:
    if i >= 2:
        continue
    else:
        print("One of the element entered is either 0 or 1 which can't be defined as prime or not prime")
        exit()

for i in inputList:
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1

    if count == 0:
        primeList.append(i)

print(primeList)
