i = 1
while i < 6:
	print(i)
	i += 1

j = 0
while j < 5:
	print(j)
	if j == 2:
		break
	#print(j)
	j += 1	

x = 0
while x < 5:
	x += 1
	if x == 3:
		continue
	print(x)
else:
	print("x is no longer greater than 5")