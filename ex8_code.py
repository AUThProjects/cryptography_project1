import crypt

#Helper function used in generation of numeric passowrds
def fillWithZeros( number):
	stringnumber = str(number)
	length = len(stringnumber)
	for i in range(6 - length):
		stringnumber = str(0) + stringnumber
	return stringnumber

givenpassword = 'ALDlgQkIyB3/I7Zcqohd2t147EBHagFE2.GHFy.zP5eAHxHbujjnCMLJvrWFqMo6LZ5g5.5eMu61tebZ/djLM.'
salt = 'ANrWqWm8'
givenpassword = "$6$"+ salt + "$" + givenpassword

for i in reversed(range(999999)): 
	password = fillWithZeros(i)
	enc = crypt.crypt(password,"$6$"+salt+"$");
	print 'Now testing: '+ str(i)
	if(enc == givenpassword):
		print 'Found! Password is ' + password
		exit()
