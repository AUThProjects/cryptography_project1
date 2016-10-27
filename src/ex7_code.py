from zipfile import *
import os

# Relevant files
input_zip_file = '../input/test_zip.zip'
output_file = '../output/test_zip'
dictionary_file = '../input/english.txt'

if __name__ == "__main__":
    z_file = ZipFile(input_zip_file)

    # Cleanup
    if os.path.isfile(output_file):
        os.remove(output_file)

    # Read dictionary
    with open(dictionary_file) as f:
        content = f.readlines()

    # bruteforce from dictionary
    secret_key = ''
    for password in content:
        try:
            # print(password)
            z_file.extractall(pwd=str.encode(password.strip()))
        except:
            pass
        if os.path.isfile(output_file) and os.path.getsize(output_file)!=0: # bug of zipfile library outputting files with zero size with wrong password
            secret_key = password;
            break # key found
        else:
            continue

    # Output
    print('Secret key is: '+secret_key)
    print('Contents of file:')
    with open(output_file, 'r') as file:
        print(file.read())
