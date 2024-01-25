'''
Write a Python program to find the numbers of words present in the given sentence.
'''

sentence = input("Enter the message sentence to find number of words in it: ")
listOfWords = []
listOfWords = sentence.split(" ")
print("The number of words in the entered sentence is: " + str(len(listOfWords)))
