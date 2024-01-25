'''
Write a Python program to generate the ticket numbers for specified number of passengers traveling in a
flight as per the details mentioned below:
The ticket number should be generated as airline:src:dest:number where,

Consider AL1 as the value for airline

src and dest should be the first three characters of the source and destination cities.

number should be auto-generated starting from 101

The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, then return the list of all generated ticket numbers.
'''

airline = "AL1"
src = str(input("Enter the 1st three letters of source airport: "))
dest = str(input("Enter the 1st three letters of destination airport: "))
numberOfPassengers = int(input("Enter the number of passengers travelling: "))

number = 100
ticketList = []
sep = "::"

while numberOfPassengers > 0:
    number += 1
    ticketList.append(airline+sep+src+sep+dest+sep+str(number))
    numberOfPassengers -= 1

print("The list of passenger ticket is")
print(ticketList)

print("The list of last 5 passenger ticket is")
print(ticketList[len(ticketList) - 5 : len(ticketList)])