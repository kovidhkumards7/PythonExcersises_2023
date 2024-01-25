def BinarySearch(arr, itbs):
    low = 0
    high = len(arr) - 1
    flag = False
    while low <= high and not flag:
        mid = (high + low) // 2
        if arr[mid] == itbs:
            flag = True
        elif itbs > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if flag:
        print("Item found")
    else:
        print("Item not found")

listOfElements = [1,45,896,215,26345,15,48,56,4,2,896,15,49,263,84]
listOfElements.sort()
searchElement = int(input("Enter the search element: "))
BinarySearch(listOfElements, searchElement)