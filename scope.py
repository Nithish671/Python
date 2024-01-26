def myFunction():
	global x
	x = 25
	print(x)

myFunction()
print(x)

def myFunction1():
	x = 25
	x -= 15 
	def myInnerFunction():
		print(x)
	myInnerFunction()

myFunction1()
