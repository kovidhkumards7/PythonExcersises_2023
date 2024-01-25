listOfElements = [3,2345, 12, 39, 24, 5]
swapCount = 0
for i in range(len(listOfElements) - 1, 0, -1):
    for j in range(i):
        if listOfElements[j] > listOfElements[j + 1]:
            temp = listOfElements[j]
            listOfElements[j] = listOfElements[j + 1]
            listOfElements[j + 1] = temp
            swapCount += 1
print("The sorted array is: ", listOfElements)
print("Number of iterations are: ", swapCount)
