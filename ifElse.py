a = 20
b = 30

if a<b:
	print("b is greater than a")

x = 25
y = 25

if x < y:
	print("y is greater than x")
elif x == y:
	print("x and y are equal")

c = 25
z = 10

if c < z:
	print("z is greater than c")
elif c == z:
	print("c and z are equal")
else:
	print("c is greater than z")

if a < b: print("b is greater than a")

print("a is greater") if a > b else print("b is greater")

print("x is greater") if x > y else print("Both equal") if x == y else print("y is greater") 

if a < b and b > c:
	print("Both conditions are true")

if a > b or b > c:
	print("Atleast one condition is true")

if not c < z:
	print("z is NOT greater than b")

s = 25

if s > 10:
	print("S is above 10")
	if s > 30:
		print("Also above 30")
	else:
		print("But, not above 30")

if c > z:
	pass