x = lambda a: a + 10
print(x(5))

x = lambda a, b : a * b
print(x(4, 3))

x = lambda a, b, c : a + (b * c)
print(x(3, 5, 7))

def myFunction(n):
	return lambda a : a * n

myDoubler = myFunction(2)

print(myDoubler(5))

def myFunction1(n):
	return lambda a : a * n

myTripler = myFunction(3)

print(myTripler(5))

def myFunction2(n):
	return lambda a : a * n

myDoubler = myFunction2(2)
myTripler = myFunction2(3)

print(myDoubler(5))
print(myTripler(5))