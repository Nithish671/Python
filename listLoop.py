animeFc = ["Naruto", "Eren", "Zoro", "Gojo"]
for x in animeFc:
   print(x)

for i in range(len(animeFc)):
	print(animeFc[i])

i = 0;
while i < len(animeFc):
	print(animeFc[i])
	i = i + 1

[print(x) for x in animeFc]

listJJK = ["Gojo", "Yuji", "Megumi", "Yuta"]
newJJK = []

for x in listJJK:
	if "u" in x:
		newJJK.append(x)

print(newJJK)

newJJK1 = [x for x in listJJK if "Y" in x]
print(newJJK1)

newJJK2 = [x for x in listJJK if x != "Megumi"]
print(newJJK2)

newJJK3 = [x for x in listJJK]
print(newJJK3)

newNumList = [x for x in range(10)]
print(newNumList)

newNumList1 = [x for x in range(10) if x > 5]
print(newNumList1)

capsJJK = [x.upper() for x in listJJK]
print(capsJJK)

helloJJK = ['hello' for x in listJJK]
print(helloJJK)

listJJKi = [x if x != "Gojo" else "Satoru" for x in listJJK]
print(listJJKi)