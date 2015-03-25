#! /usr/env/python

text = 'ΟΚΗΘΜΦΔΖΘΓΟΘΧΥΚΧΣΦΘΜΦΜΧΓΟΣΨΧΚΠΦΧΘΖΚΠ'
text2 = list(text)
text_int = list(text)
# for i in range(25):
#     for j in range(0,len(text)):
#         text2[j] = chr((ord(text[j])+i-913)%25+913)
#         if ord(text[j])<930 and ord(text[j])+i>=930:
#             # text2[j] = chr((ord(text2[j])+1-913)%25+913)
#             text2[j] = chr((ord(text[j])+i+1-913)%25+913)
#     print(i)
#     print(''.join(text2))
# # for i in range(25):
# #     print(chr(i+913))
#

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
    
# print(let_to_int)
# print(int_to_let)

for i in range(len(text)):
    text_int[i] = let_to_int[text[i]]
    
for i in range(25):
    for j in range(len(text)):
        text2[j] = int_to_let[(text_int[j]+i)%24]
    print(''.join(text2))
    