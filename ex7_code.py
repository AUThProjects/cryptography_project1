from zipfile import *
import os

# Relevant files
input_zip_file = 'test_zip.zip'
output_file = 'test_zip'
dictionary_file = 'english.txt'

z_file = ZipFile(input_zip_file)

# cleanup
if os.path.isfile(output_file):
    os.remove(output_file)

# read dictionary
with open(dictionary_file) as f:
    content = f.readlines()

# bruteforce from dictionary
secret_key = ''
for password in content:
    try:
        print(password)
        z_file.extractall(pwd=str.encode(password.strip()))
    except:
        pass
    if os.path.isfile(output_file) and os.path.getsize(output_file)!=0:
        secret_key = password;
        break # key found
    else:
        continue

# Output
print('Secret key is: '+secret_key)
print('Contents of file:')
with open(output_file, 'r') as file:
    print(file.read())