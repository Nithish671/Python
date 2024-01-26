jjkSet = {"Yuta", "Panda", "Inumaki", "Gojo"}
print(jjkSet)

exSet = {"Luffy", "Zoro", True, 1, 0, False, 2}
print(exSet)
print(len(exSet))

exSet1 = {"abc", 123, 1.2, False}
print(exSet1)
print(type(exSet))

narutoSet = set(("Naruto", "Kakashi", "Sasuke"))
print(type(narutoSet))

for x in narutoSet:
	print(x)

print("Kakashi" in narutoSet)

if "Kakashi" in narutoSet:
	print("Copy Ninja is present on the set")

jjkSet.add("Geto")
print(jjkSet)

jjkSet.update(narutoSet)
print(jjkSet)

jjkList = ["Yuji", "Megumi", "Ryomen"]
jjkSet.update(jjkList)
print(jjkSet)

jjkSet.remove("Naruto")
jjkSet.discard("Zoro")
print(jjkSet)
x = jjkSet.pop()
print(x)

#jjkSet.clear()
print(jjkSet)
#del jjkSet
print(jjkSet)

animeSet = {"Luffy", "Naruto", "Zoro", "Sasuke", "Gojo"}
opSet = {"Luffy", "Zoro", "Usopp", "Sanji"}
#animeSet.union(opSet)
animeSet1 = animeSet.union(opSet)
print(animeSet1)

#animeSet.intersection_update(opSet)
#animeSet2 = animeSet.intersection(opSet)
#print(animeSet2)

#animeSet.symmetric_difference_update(opSet)
animeSet3 = animeSet.symmetric_difference(opSet)
print(animeSet3)