#!/usr/bin/env python3

import crypt

# Helper function used in padding a number with zeros
def fillWithZeros(number):
	stringnumber = str(number)
	length = len(stringnumber)
	for i in range(6 - length):
		stringnumber = str(0) + stringnumber
	return stringnumber

enc_password = 'ALDlgQkIyB3/I7Zcqohd2t147EBHagFE2.GHFy.zP5eAHxHbujjnCMLJvrWFqMo6LZ5g5.5eMu61tebZ/djLM.'
salt = 'ANrWqWm8'
enc_password = "$6$"+ salt + "$" + enc_password

# Start guessing from the end (ends sooner!)
for i in reversed(range(999999)): 
	password = fillWithZeros(i)
	enc = crypt.crypt(password,"$6$"+salt+"$");
	# print('Now testing: '+ str(i))
	if enc == enc_password:
		print('Found! Password is ' + password)
		exit()
