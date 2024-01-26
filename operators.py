a = 25
b = 6
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

a += b
print(a)

x = 5
x &= 3
print(x)

y = 5
y |= 6
print(y)

x = 5
x ^= 3
print(x)

print(x <= 6)
print(x > 2 and x < 10)
print(x > 10 or x < 10)
print(not(x > 10 or x < 10))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
print(x is not y)
print(x != y)

print(x is z)
print(x is y)
print(x == y)

print("pineapple" in x)
print("pineapple" not in x)

print(5 & 2)
print(4 | 8)
print(3 ^ 2)
print(~2)
print(8>>2)
print(8<<2)