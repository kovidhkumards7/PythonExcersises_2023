word = input("Enter a word to find it is Palindrome or not: ")
list = []
list.extend(word)
list1 = list
list = list[::-1]

print("The reverse of list is: ", end=" ")
for i in list:
    print(i, end="")
print()

if list == list1:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
