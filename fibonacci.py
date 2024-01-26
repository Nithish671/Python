def fibonacciSeries(n):
	fibSeries = [0, 1]

	while len(fibSeries) < n:
		nextNum = fibSeries[-1] + fibSeries[-2]
		fibSeries.append(nextNum)

	return fibSeries

#print(fibonacciSeries(10))
numTerms = 10
result = fibonacciSeries(numTerms)
print(result)