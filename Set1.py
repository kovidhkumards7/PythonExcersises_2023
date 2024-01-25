'''
Write a python function find_common_characters(msg1,msg2) to display all the common characters between
given two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

Example: msg1="I like Python", msg2="Java is a very popular language" output=lieyon
'''

sentence1 = input("Enter sentence 1: ")
sentence2 = input("Enter sentence 2: ")

def find_common_characters(msg1, msg2):
    msg1 = msg1.lower()
    msg2 = msg2.lower()
    list1 = []
    list2 = []
    msg1 = msg1.replace(" ","")
    msg2 = msg2.replace(" ","")
    list1.extend(msg1)
    list2.extend(msg2)
    set1 = set(list1)
    set2 = set(list2)
    set3 = set2.intersection(set1)
    if len(set3) == 0:
        return -1
    else:
        return (set3)

common = find_common_characters(sentence1, sentence2)
commonString =""
for i in common:
    commonString += i
print("The common characters in both of the messages are: ", commonString)
