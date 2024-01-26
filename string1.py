age = 20
txt = "My name is Itachi, and I am {} years old."
print(txt.format(age))

quantity = 3
itemNo = 567
price = 25.12
myOrder = "I want {} pieces of item {} for {} dollars"
print(myOrder.format(quantity, itemNo, price))

swords = 3
age = 21
crew = 9
zoro = "I am Zoro,\n I am {1} years old, I have {0} swords and i am using {0} sword style and my crew has {2} members"
print(zoro.format(swords, age, crew))

print("I am Luffy\r I ate \"Gum-Gum\" fruit and \tI am \"RubberMan\"")