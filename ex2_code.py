#/usr/bin/env python3

# RC4 Encryption implementation

# Key Scheduling Algorithm
def KSA(key):
	S = []
	for i in range(0, 256):
		S.append(i)
	j = 0
	for i in range(0, 256):
		j = (j + S[i] + ord(key[i%len(key)]))%256
		swap(S, i, j)
	return S

# Pseudo-random Generation Algorithm
def PRGA(plaintext, S):
	i = 0
	j = 0
	k = []
	plaintext_length = len(plaintext)
	while plaintext_length > 0:
		i = (i+1)%256
		j = (j+S[i])%256
		swap(S, i, j)
		k.append(S[(S[i]+S[j])%256])
		plaintext_length -= 1
	return k

# Encryption function
def encrypt(K, plaintext):
	plaintext_bin = []
	counter = 0
	output = []
	for character in plaintext:
		plaintext_bin.append(ord(plaintext[counter]))
		output.append(plaintext_bin[counter] ^ K[counter])
		counter += 1
	return output

# Swapping letter function
def swap(S, i, j):
	temp = S[i]
	S[i] = S[j]
	S[j] = temp

if __name__ == "__main__":
	key = "MATRIX"
	text = "Never send a human to do a machine s job"
	S = KSA(key)
	k = PRGA(text, S)
	encrypted = encrypt(k, text)
	for number in encrypted:
		print(format(number, '02x'), end=" ")
	print("")
