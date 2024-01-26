def my_function():
	print("Hello from function")

my_function()

def myFunction(fname):
	print(fname + " Uchiha")

myFunction("Itachi")
myFunction("Sasuke")

def myFunction1(fName, lName):
	print(fName + " " + lName)

myFunction1("Sano", "Manjiro")
#myFunction1("Mikey")

def myFunction2(*members):
	print("The Uchiha clan member is " + members[2])
	print("The clan leader is " + members[0])
myFunction2("Madara", "Obito", "Itachi")

def myFunction3(cap, vc, cook):
	print("The Captain is " + cap)
	print("The vice-Captain is " + vc)

myFunction3(cap = "Luffy", vc = "Zoro", cook = "Sanji")

def myFunction4(**name):
	print("The first name is " + name["fName"])
	print("The last name is " + name["lName"])

myFunction4(lName = "Roronoa", fName = "Zoro")

def my_function1(country = "India"):
	print("I am from " + country)

my_function1("Hidden Leaf")
my_function1()

def my_function2(food):
	for x in food:
		print(x)

fruits = ["Apple", "Orange", "Cherry"]

my_function2(fruits)

def my_function3(x):
	return 5 * x
	#print(x)

print(my_function3(2))
#my_function3(4)

def my_function4():
	pass

def tri_recursion(k):
	if k > 0:
		result = k + tri_recursion(k - 1)
		print(result)
	else:
		result = 0
	return result

print("/n/nRecursion Example Result: ")

tri_recursion(6)