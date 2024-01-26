b = "Hello World"
print(b[2:8])
print(b[:6])
print(b[2:])
print(b[-7:-2])
print(b.upper())
print(b.lower())

c = "   Hello, World   "
print(c.strip())
print(c.replace("H", "K"))
print(c.split(","))

print("Hello")
print('Hello')
a = "Hello"
print(a)

a = """Itachi is pure evil,
who slaughtered his clan and
became akatsuki.but, thats not 
the truth itachi killed his clan for his village
he stand between village and clan.""" 
b = '''Itachi get disgrace in the place of honor,
hate in the place of love.but, he still protected 
his village.'''
print(a)
print(b)
print("Itachi" in a)
print("Sasuke" not in a)

if "akatsuki" in a:
	print("Yes, 'akatsuki' present in a");

if "Sasuke" not in a:
	print("Sasuke not present in a");

x = "Sasuke"
print(x[1])
print(len(x))

for x in "Madara":
  print(x)

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

a = "Hello"
b = " World"
c = a + b
print(c)