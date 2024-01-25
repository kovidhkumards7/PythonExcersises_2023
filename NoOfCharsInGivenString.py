'''
Write a Python program to find the number of characters present the given string.
'''

sentence = input("Enter the message sentence to find number of chars: ")
count = 0
for i in sentence:
    if i != " ":
        count += 1
print("The number of chars in the entered sentence is: " + str(count))
print(len(sentence))