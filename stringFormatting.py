price = 25
txt = "The price is {} dollars"
print(txt.format(price))

txt1 = "the price is {:.2f} dollars"
print(txt1.format(price))

quantity = 10
no = 200
price = 25
myOrder = "I want {} pieces of number {} for {:.2f} dollars"
print(myOrder.format(quantity, no, price))

myIndexOrder = "I want {2} pieces of number {0} for {1:.2f} dollars"
print(myIndexOrder.format(no, price, quantity))

name = "Roronoa Zoro"
age = 21
zoro = "His name is {1}. {1} is {0} years old."
print(zoro.format(age, name))

car = "I have {brand}, It is a {model} model."
print(car.format(brand="Audi", model="A8"))