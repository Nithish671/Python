class Person:
	def __init__(self, fName, lName):
		self.firstName = fName
		self.lastName = lName

	def printName(self):
		print(self.firstName, self.lastName)

x = Person("Itachi", "Uchiha")
x.printName()

class Student(Person):
	pass

x = Student("Sasuke", "Uchiha")
x.printName()

class Student1(Person):
	def __init__(self, fName, lName):
		#Person.__init__(self, fName, lName)
		super().__init__(fName, lName)
		self.graduationYear = 2023

x = Student1("Obito", "Uchiha")
x.printName()
print(x.graduationYear)

class Student2(Person):
	def __init__(self, fName, lName, year):
		super().__init__(fName, lName)
		self.graduationYear = year

	def myFunction(self):
		print("Welcome", self.firstName, self.lastName,"from", self.graduationYear)

x = Student2("Naruto", "Uzumaki", 2023)
x.myFunction()