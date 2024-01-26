thisList = ["apple", "banana", "cherry", "apple", "banana"]
print(len(thisList))

list1 = ["Madara", "Itachi", "Sasuke"]
list2 = [3, 1, 43, 25]
list3 = [True, False, False]

list4 = ["abc", 25, True, 40, "Male"]

print(list1)
print(list2)
print(list3)
print(list4)
print(type(list4))

thislist1 = list(("Luffy", "Zoro", "Sanji", "Chopper", "Usopp", "Franky"))
print(thislist1)
print(thislist1[1])
print(thislist1[-2])
print(thislist1[2:6])
print(thislist1[:4])
print(thislist1[2:])
print(thislist1[-4:-1])

if "Zoro" in thislist1:
	print("Zoro is in the list")