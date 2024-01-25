'''
Write a python function, encrypt_sentence(msg) which accepts a message and encrypts it based on rules given below and
returns the encrypted message.

Words at odd position -> Reverse It

Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order
should not change

Note: Assume that the sentence would begin with a word and there will be only a single space between the words.

          Perform case sensitive string operations wherever necessary.

Example: msg=the sun rises in the east    output=eht snu sesir ni eht stea
'''

sentence = input("Enter the message sentence to encrypt it: ")

def encrypt(message):
    message = message.lower()
    listOfWords = []
    listOfWords = message.split(" ")
    vowels = "aeiou"
    consonents = "bcdfghjklmnpqrstvwxyz"

    for i in range(0, len(listOfWords), 2):
        listOfWords[i] = listOfWords[i][::-1]

    for i in range(1, len(listOfWords), 2):
        word = listOfWords[i]
        newWord = ""

        for letter in word:
            if letter in consonents:
                newWord += letter

        for letter in word:
            if letter in vowels:
                newWord += letter

        listOfWords[i] = newWord

    finalSentence = ""
    for listWord in listOfWords:
        finalSentence += listWord + " "

    return finalSentence

print(encrypt(sentence))