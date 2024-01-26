narutoTuple = ("Naruto", "Sasuke", "Kakashi")

myIt = iter(narutoTuple)

for a in narutoTuple:
	print(a)

print(next(myIt))
print(next(myIt))
print(next(myIt))

x = "Madara Uchiha"
myIt1 = iter(x)

for b in x:
	print(b)

print(next(myIt1))
print(next(myIt1))
print(next(myIt1))
print(next(myIt1))
print(next(myIt1))
print(next(myIt1))

class myNumbers:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		if self.a <= 20: 
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration

myClass = myNumbers()
myIter = iter(myClass)

for x in myIter:
	print(x)

