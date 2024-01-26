tupleAOT = ("Eren", "Mikasa", "Levi", "Armin")
x = list(tupleAOT)
print(type(x))
print(x)
x[1] = "Zeke"
tupleAOT = tuple(x)
print(type(tupleAOT))
print(tupleAOT)

y = list(tupleAOT)
y.append("Mikasa")
tupleAOT = tuple(y)
print(tupleAOT)

z = ("Bertholdt", )
tupleAOT += z
print(tupleAOT)

a = list(tupleAOT)
a.remove("Bertholdt")
tupleAOT = tuple(a)
print(tupleAOT)

#del tupleAOT
print(tupleAOT)
(c1, c2, c3, c4, c5) = tupleAOT
#print(c1)
print(c3)

(mainC, *sideC, mainC1) = tupleAOT
print(mainC)
print(sideC)

for x in tupleAOT:
	print(x)

for i in range(len(tupleAOT)):
	print(tupleAOT[i])

i = 0
while i < len(tupleAOT):
	print(tupleAOT[i])
	i += 1

tupleDS = ("Tanjiro", "Inosuke", "Zenitsu")
anime = tupleAOT + tupleDS
print(anime)

tupleDS1 = tupleDS * 2
print(tupleDS1)
print(tupleDS1.count("Inosuke")) 
print(tupleDS1.index("Zenitsu"))


