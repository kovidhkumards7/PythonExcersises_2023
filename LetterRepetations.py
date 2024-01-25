'''
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function encode(message)  which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program.

Example: message=AAAABBBBCCCCCCCC  output: 4A4B8C
'''

inputString = input("Enter the string: ")
list = []
list.extend(inputString)
list1 = set(list)
for i in list1:
    if i == " " or i == "." or i == ",":
        continue
    else:
        print(inputString.count(i), i, end="", sep="")

