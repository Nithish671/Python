class MyClass:
	x = 5

print(MyClass)

p1 = MyClass()
print(p1.x)

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

person1 = Person("Itachi", 20)

print(person1.name)
print(person1.age)

class Name:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name}({self.age})"

name1 = Name("Sasuke", 17)
print(name1)

class MyClass1:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def myFunction(self):
		print("My name is" , self.name , "and my age is" , self.age)

c1 = MyClass1("Gojo", 25)
c1.myFunction()

class Person2:
	def __init__(iObject, name, age):
		iObject.name = name
		iObject.age = age

	def myFunction(abc):
		print("Hello my name is", abc.name, "\nMy age is", abc.age)

o1 = Person2("Luffy", 20)
o1.myFunction()
#del o1
o1.age = 17
#del o1.age
o1.myFunction()

class Person3:
	pass