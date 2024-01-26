narutoDict = {
	"name" : "Naruto",
	"age" : "20",
	"eyeColor" : "Blue"
}

for x in narutoDict:
	print(x)
	print(narutoDict[x])

for x in narutoDict:
	print(narutoDict[x])

for x in narutoDict.values():
	print(x)

for x in narutoDict.keys():
	print(x)

for x,y in narutoDict.items():
	print(x, y)

narutoDict1 = narutoDict.copy()
print(narutoDict1)

narutoDict2 = dict(narutoDict1)
print(narutoDict2)

