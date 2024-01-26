thisList = ["Zoro", "Luffy", "Sanji", "Franky"]
thisList[3] = "Chopper"
print(thisList)

thisList[2:4] = ["Usopp", "Franky", "Chopper", "Brook"]
print(thisList)

thisList[2:4] = ["Robin"]
print(thisList)

thisList.insert(2, "Sanji")
print(thisList)

thisList.append("Nami")
print(thisList)

thisList1 = ["Naruto", "Kakashi", "Sasuke"]
thisList.extend(thisList1)
print(thisList)

thisTuple = ("Gojo", "Yuji", "Megumi")
thisList.extend(thisTuple)
print(thisList)

thisList.remove("Nami")
print(thisList)

thisList.pop(3)
print(thisList)

thisList.pop()
print(thisList)

del thisList[5]
print(thisList)

#del thisList
thisList.clear()
print(thisList)