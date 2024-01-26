try:
	f = open("demoFile.txt")
	try:
		f.write("Wake up to Reality...")
	except:
		print("Something went wrong when writing to the file")
	finally:
		f.close()
except:
	print("Something went wrong when opening the file")

try:
	print(x)
except:
	print("An error occured")

try:
	print(a)
except NameError:
	print("Variable a is not defined")
except:
	print("Something else went wrong")

try:
	print("Hello")
except:
	print("Something went wrong")
else:
	print("Nothing went wrong")

try:
	print(b)
except:
	print("Something went wrong")
finally:
	print("The 'try except' is finished")