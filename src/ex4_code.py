#! /usr/bin/env python3 

# Shift cipher code


text = 'ΟΚΗΘΜΦΔΖΘΓΟΘΧΥΚΧΣΦΘΜΦΜΧΓΟΣΨΧΚΠΦΧΘΖΚΠ'
text2 = list(text)
text_int = list(text)

# Create two invert with each other hashes for Greek uppercase letter-int dictionary (due to inconsistence of sigm inside the ASCII table)
let_to_int = {}
int_to_let = {}

for i in range (25):
    if 913+i > 930:
        let_to_int[chr(913+i)] = i-1
        int_to_let[i-1] = chr(913+i)
    elif 913+i == 930:
        continue
    else:
        let_to_int[chr(913+i)] = i
        int_to_let[i] = chr(913+i)


for i in range(len(text)):
    text_int[i] = let_to_int[text[i]]


if __name__=="__main__":    
    for i in range(25):
        for j in range(len(text)):
            text2[j] = int_to_let[(text_int[j]+i)%24]
        print(''.join(text2))