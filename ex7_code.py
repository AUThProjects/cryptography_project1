from zipfile import *

z_file = ZipFile("test_zip.zip")

with open('english.txt') as f:
    content = f.readlines()
    
# print(content[1])
for password in content:
    try:
        print(password)
        z_file.extractall(pwd=str.encode(password.strip()))
    except RuntimeError:
        pass