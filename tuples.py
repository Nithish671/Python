tupleJJK = ("Gojo", "Gojo", "Yuji", "Yuta", "Fushiguro")
print(tupleJJK)
print(len(tupleJJK))

tupleAOT = ("Eren",)
print(type(tupleAOT))

tupleData = ("abc", 123, False, 3.4, "male")
print(tupleData)

tupleOP = tuple(("Luffy", "Zoro", "Sanji", "Usopp", "Chopper", "Franky"))
print(tupleOP)
print(type(tupleOP))
print(tupleOP[1])
print(tupleOP[-1])
print(tupleOP[1:2])
print(tupleOP[:2])
print(tupleOP[1:])
print(tupleOP[-5:-2])

if "Zoro" in tupleOP:
	print("SwordsMan not lost yet...")