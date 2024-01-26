uchiha = ["Madara", "Obito", "Itachi", "Sasuke"]
for x in uchiha:
	print(x)

jjk = "Gojo Satoru"
for y in jjk:
	print(y)

op = ["Luffy", "Zoro", "Sanji", "Usopp"]
for a in op:
	print(a)
	if a == "Zoro":
		break

for b in op:
	if b == "Usopp":
		break
	print(b)

naruto = ["Naruto", "Sasuke", "Kakashi", "Itachi", "Jiraiya"]
for x in naruto:
	if x == "Sasuke":
		continue
	print(x)

for y in range(5):
	print(y)

for b in range (2, 5):
	print(b)

for z in range(0, 25, 10):
	print(z)

for x in range(5):
	print(x)
else:
	print("Finally Finished")

for y in range(5):
	if y == 2: break
	print(y)
else:
	print("Finally Stopped")

name = ["Naruto", "Sasuke", "Kakashi"]
clan = ["Uzumaki", "Uchiha", "Hatake"]

for x in name:
	for y in clan:
		print(x + " from " + y + " clan.")

for x in [0, 1, 2]:
	pass