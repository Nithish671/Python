jjkDict = {
	"name" : "Gojo",
	"age" : 25,
	"eyeColor" : "Blue"
}

narutoDict = dict(name = "Itachi", age = 20, eyeColor = "Red")
jjkDict["name"] = "Satoru"
print(jjkDict)

jjkDict.update({"name" : "Gojo"})
print(jjkDict)

jjkDict["CT"] = "Limitless & Six eyes"
print(jjkDict)

jjkDict.update({"nation" : "Japan"})
print(jjkDict)

jjkDict.pop("CT")
print(jjkDict)

jjkDict.popitem()
print(jjkDict)

del jjkDict["eyeColor"]
print(jjkDict)

jjkDict.clear()
print(jjkDict)

del jjkDict
print(jjkDict)