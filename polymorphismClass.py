class Car:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

	def move(self):
		print("Drive")

class Boat:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

	def move(self):
		print("Sail")

class Plane:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

	def move(self):
		print("Fly")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
	x.move()

class Vehicle:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model

	def move(self):
		print("Move")

class Car1(Vehicle):
	pass

class Boat1(Vehicle):
	def move(self):
		print("Sail")

class Plane1(Vehicle):
	def move(self):
		print("Fly")

car2 = Car1("Audi", "A8")
boat2 = Boat1("Ibiza", "Touring 20")
plane2 = Plane1("Boeing", "747")

for x in (car2, boat2, plane2):
	print(x.brand)
	print(x.model)
	x.move()