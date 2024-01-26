jjkDict = {
	"name" : "Gojo",
	"age" : 25,
	"eyeColor" : "Blue",
	"age" : 20
}

print(jjkDict)
print(jjkDict["eyeColor"])
print(len(jjkDict))

exDict = {
	"name" : "abc",
	"age" : 123,
	"tf" : False,
	"colors" : ["Blue" ,"Black"]
}

print(exDict)
print(type(exDict))

opDict = dict(name = "Zoro", age = 20, role = "SwordsMan")
print(opDict)
x = opDict["role"]
y = opDict.get("name")
print(x)
print(y)
z = opDict.keys()
print(z)

opDict["swordName"] = "Enma"

print(z)

a = opDict.values()
print(a)

i = opDict.items()
print(i)

opDict["birthday"] = "NOV, 11"

print(i)

opDict["swordName"] = "Kitetsu"
print(i)

if "age" in opDict:
	print("Yes, age is one of the key")