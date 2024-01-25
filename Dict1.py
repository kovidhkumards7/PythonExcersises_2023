'''
Write a Python function words_count(sentence) to return a dictionary with the length of words as key
and number words with such length as value.

Example: sentence=“I love python and it so easy to learn” sample output={1:1,4:2,5:1,3:1,2:3,6:1}
'''

sentence = input("Enter the message sentence: ")

def words_count(sentence):
    listSentence = []
    listSentence = sentence.split(" ")
    dict = {}

    for word in listSentence:

        count = 0

        for compareWord in listSentence:

            if len(word) == len(compareWord):
                count += 1

        dict[len(word)] = count

    return dict

print(words_count(sentence))