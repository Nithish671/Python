x = "Awesome"

def myFunc():
 print("Python is ", x)
 print("Python is " + x);
myFunc()

print("Python is " + x)

def myFunc1():
  global x
  x = "Fantastic"
  print("python is " + x)
myFunc1()

print("Python is " + x)