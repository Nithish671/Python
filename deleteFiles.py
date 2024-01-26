import os

if os.path.exists("demoFile2.txt"):
	os.remove("demoFile2.txt")
else:
	print("File doesn't exist")

os.rmdir("demo")