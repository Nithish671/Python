f = open("demoFile.txt")

f = open("demoFile.txt", "rt")

d = open("C:\\Users\\NITHISH\\Documents\\New folder\\demoFile.txt", "r")
print(d.read(10))
print(d.read())
#d.close()
print(d.readline())
print(d.readline())

for x in f:
	print(x)

f.close()
d.close()

f = open("demoFile.txt", "a")
f.write("The line written using f.write")
f.close()

f = open("demoFile.txt", "r")
print(f.read())

f.close()

f = open("demoFile1.txt", "w")
f.write("The contents are replaced using \"w\" write method")
f.close()

f = open("demoFile1.txt", "r")
print(f.read())
f.close()

#f1 = open("demoFile1.txt", "x")
f1 = open("demoFile2.txt", "a")
f1.write("Wake up to Reality!")
f1.close()

f1 = open("demoFile2.txt", "r")
print(f1.read())
f1.close()

f2 = open("demoFile2.txt", "w")
f2.write("I will make my fantasy into Reality!")
f2.close()

f2 = open("demoFile2.txt", "r")
print(f2.read())
f2.close()



