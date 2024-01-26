import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

y = datetime.datetime(2000, 10, 25)
print(y)
print(y.strftime("%B"))
