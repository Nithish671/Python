import json

x = '{"name" : "Gojo", "age" : 25, "city" : "Japan"}'

y = json.loads(x)

print(y["age"])

opDict = {
	"name" : "Zoro",
	"age" : 21,
	"city" : "Wano"
}

a = json.dumps(opDict)

print(a)

print(json.dumps(["Itachi", "Sasuke"]))
print(json.dumps(("Eren", "Levi")))
print(json.dumps("Hello"))
print(json.dumps(25))
print(json.dumps(2.5))
print(json.dumps(True))
print(json.dumps(None))

opDic = {
	"name" : "Zoro",
	"age" : 21,
	"haki" : True,
	"married" : False,
	"hakiTypes" : ("Conqueror", "Armament", "observation"),
	"pets" : None,
	"Swords" : [
	{"swordName" : "Ichimonji", "grade" : 8.4},
	{"swordName" : "Shusui", "grade" : 9.5}
	]
}

print(json.dumps(opDic, indent=4, separators=(" . ", " = "), sort_keys=True))