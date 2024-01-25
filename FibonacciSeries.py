numberOfTerms = int(input("Enter the  number of terms required in a fibonacci series: "))
firstTerm = 0
secondTerm = 1
thirdTerm = 0
fibonacciSeries = [0, 1]
for term in range(3, numberOfTerms + 1):
    thirdTerm = firstTerm + secondTerm
    fibonacciSeries.append(thirdTerm)
    firstTerm = secondTerm
    secondTerm = thirdTerm
print("The fibonacci series are : ")
for term in fibonacciSeries:
    print(term, end="    ")