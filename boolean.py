print(10<9)
print(10>9)
print(10==9)

n = 20
s = 22

if n > s:
  print("N is greater than S")
else:
  print("S is greater than N") 


print(bool("Hello"))
print(bool(25))

x = "Hello"
y = 25

print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(0))
print(bool(""))
print(bool(None))
bool(())
bool([])
bool({})

class myClass():
	def __len__(self):
		return 0

myObj = myClass()
print(bool(myObj))

class myClass1():
	def _len_(self):
		return 0

myObj1 = myClass1()
print(bool(myObj1))


def myFunction() :
	return True

print(myFunction())


if myFunction(): 
	print("Yes!")
else:
	print("No!")

x = 200
print(isinstance(x, int))
