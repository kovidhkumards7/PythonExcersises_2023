'''
Write a Python function vowel_count(sentence) to return a dictionary with vowels, consonants,
others as key and respective number of vowels, consonants, others characters as value.

Note: Do case insensitive operations

Example: sentence=“I love python and it so easy to learn”

                 sample output={“vowels”:12,”consonants”:17, “others”:8}
'''

sentence = input("Enter the message sentence: ")

def vowel_count(sentence):

    sentence = sentence.lower()
    vowels = "aeiou"
    consonents = "bcdfghjklmnpqrstvwxyz"
    dict = {"vowels":0,
            "consonents":0,
            "others":0}

    for i in sentence:
        if i in vowels:
            dict["vowels"] += 1
        elif i in consonents:
            dict["consonents"] += 1
        else:
            dict["others"] += 1

    return dict

print(vowel_count(sentence))