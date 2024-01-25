#lex_auth_0127667342200995843410
def make_change(denomination_list, amount):
    '''Remove pass and implement the Greedy approach to make the change for the amount using the
    currencies in the denomination list.
    The function should return the total number of notes needed to make the change. If change
    cannot be obtained for the given amount, then return -1. Return 1 if the amount is equal to
    one of the currencies available in the denomination list.  '''
    denomination_list.sort()
    denomination_list = denomination_list[::-1]
    denominationDict = dict()
    for i in denomination_list:
        denominationDict[i] = 0
    for i in denomination_list:
        if i > amount:
            continue
        else:
            denominationDict[i] = amount // i
            amount = amount % i
    print(denominationDict)
    if amount == 0:
        return 1
    else:
        return -1


#Pass different values to the function and test your program
amount= 20
denomination_list = [1,15,10]
make_change(denomination_list, amount)
make_change(amount=10,denomination_list=[2, 4, 6, 8, 10])