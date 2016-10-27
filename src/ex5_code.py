#/usr/bin/env python3

from Crypto.Cipher import AES
import binascii
import copy
import string
import random



# Avalanche effect in AES

NUMBER_OF_INPUTS = 80 # Number of inputs from which we gather results

# Encrypt message with AES
def encrypt(key, bin_message):
	obj = AES.new(key, AES.MODE_ECB)
	ciphertext1 = binascii.hexlify(obj.encrypt(bin_message))
	ciphertext = bin(int(ciphertext1, 16))[2:]
	ciphertext = '0000000000000000'[:128-len(ciphertext)] + ciphertext # padding to the front for having the same length in ciphertexts
	return ciphertext


# Measure the number of different bits between two encrypted messages
def bin_distance(key, message1, message2):
	# message 1 and message 2 MUST have the same length and differ by one bit
	ciphertext1 = encrypt(key, message1)
	ciphertext2 = encrypt(key, message2)
	counter = 0
	counter_step = 0
	for character in ciphertext1:
		if ciphertext1[counter_step] != ciphertext2[counter_step]:
			counter += 1
		counter_step += 1
	return counter

# Generate a random string
def string_gen(size=16, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

# Convert string to bitstring
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

# Convert bistring to string
def frombits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

if __name__ == "__main__":
	samples = []
	samples_diff = []
	for i in range(NUMBER_OF_INPUTS):
		samples.append(string_gen())

	samples_diff = []
	for i in range(NUMBER_OF_INPUTS):
		bitstring = tobits(samples[i])
		position_to_change = random.randint(0, len(bitstring)-1)
		bitstring_list = list(bitstring)
		if bitstring_list[position_to_change] == 0:
			bitstring_list[position_to_change] = 1
		else:
			bitstring_list[position_to_change] = 0
		samples_diff.append(frombits(bitstring_list))

	results = []
	for i in range(NUMBER_OF_INPUTS):
		try:
			results.append(bin_distance(b"somethinsomethin", samples[i], samples_diff[i]))
		except: # We opt for not catching the errors due to different lengths of strings in the Greek language
			pass

	print("The average number of different bits measured by "+str(len(results))+" messages is:")
	print(sum(results)/len(results))