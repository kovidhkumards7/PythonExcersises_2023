'''
Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary

{"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

and use it to translate your Christmas wishes from English into Swedish.

That is, write a Python function translate(b_dict,list_words) that accepts the bilingual dictionary and a list of
English words (your Christmas wish) and returns a list of equivalent Swedish words.
'''

def translate(b_dict, list_words):
    translatedList = []
    for i in list_words:
        translatedList.append(b_dict[i])
    return translatedList

dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
words = input("Enter message: ")
word = words.split(" ")
trans = list(translate(dict, word))
for i in trans:
    print(i, end=" ")
