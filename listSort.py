naruto = ["Naruto", "Sasuke", "Kakashi", "Jiraiya", "Minato"]
naruto.sort(reverse = True)
print(naruto)
naruto.reverse()
print(naruto)

def myFunction(n):
	return abs(n - 50)

myNum = [45, 53, 72, 50, 67, 88]
myNum.sort(key = myFunction)
print(myNum)

fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.sort()
print(fruits)
fruits.sort(key = str.lower)
print(fruits)

anime = ["Luffy", "Eren", "Zoro", "Naruto"]
anime1 = anime.copy()
print(anime1)

anime2 = list(anime1)
print(anime2)

animeCom = naruto + anime
print(animeCom)

for x in naruto:
	anime.append(x)

print(anime)

jujutsu = ["Gojo", "Yuta", "Fushiguro", "Yuji"]
anime.extend(jujutsu)
print(anime)