'''
Given a list of integer values, write a Python program to check whether the list contains the same number
in adjacent positions. Display the count of such adjacent occurrences.

Sample Input                    Sample Output
[1,1,5,100,-20,-20,6,0,0]       3

[10,20,30,40,30,20]             0

[1,2,2,3,4,4,4,10]              3
'''

list = [1,2,2,3,4,4,4,10]
print(len(list))
count = 0
for size in range(0,len(list) - 1):
    if list[size] == list[size + 1]:
        count += 1
print("The number of occurences of repeated elements is: ", str(count))