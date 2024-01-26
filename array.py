cars = ["Ford", "Volvo", "BMW"]
print(cars)

x = cars[1]
print(x)

cars[0] = "Toyota"
print(cars)

print(len(cars))

for x in cars:
	print(x)

cars.append("Audi")
print(cars)

cars.pop(0)

print(cars)

cars.remove("BMW")
print(cars)