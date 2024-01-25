'''
Write a python function, find_pairs_of_numbers(num_list,n) which accepts a list of positive integers with no
repetitions and returns count of pairs of numbers in the list that adds up to n. The function should return 0,
if no such pairs are found in the list.

Example: num_list=[1, 2, 7, 4, 5, 6, 0, 3], n=6 output:3

         num_list= [3, 4, 1, 8, 5, 9, 0, 6], n=9 output:4
'''

def find_pairs_of_numbers(num_list, n):
    num_list = set(num_list)
    num_list = list(num_list)
    sumList = 0

    for i in num_list:
        for j in num_list:
            if i == j:
                continue
            else:
                if i + j == n:
                    sumList += 1
                    # num_list.remove(i)
                    # num_list.remove(j)
                    continue

    return sumList

print(int(find_pairs_of_numbers([3, 4, 1, 8, 5, 9, 0, 6],9)/2))
print(int(find_pairs_of_numbers([1, 2, 7, 4, 5, 6, 0, 3],6)/2))