from os import remove

def encryption(name, file, key):
    key_list = str(key)
    encrypted_file = ""
    i = 0
    for c in str(file):
        encrypted_file += chr(ord(c) + int(key_list[i]))
        i+=1
        if i > 3:
            i = 0
    file = open(name, "w")
    file.write(encrypted_file)
    file.close()
    return file


def decryption(name, encrypted_file, key):
    key_list = str(key)
    file = ""
    i = 0
    for c in str(encrypted_file):
        file += chr(ord(c) - int(key_list[i]))
        i += 1
        if i > 3:
            i = 0
    encrypted_file = open(name, "w")
    encrypted_file.write(file)
    encrypted_file.close()
    return encrypted_file


def read_file(name, file):
    file = open(name, "r")
    file = file.read()
    return file


def delete_file(file):
    remove(file)
