from crypt import *
from utils import *
from datetime import datetime
from os import path
import send_mail
import socket

now = datetime.now()

logs = open("logs.txt", "a")

logs.write("\n[" + str(now.strftime("%d/%m/%Y %H:%M:%S")) + "]" + "- A user has started the software")

logs.close()

login_success = False

user_try = 5

logs = open("intrusion_log.txt", "r")
print(logs.read())
log_text = logs.read()



"""
if len(log_text) != 0:
    user_input = input("The software is locked, please contact an administrator or enter the 4 digits key (0000) to unlock.\n")
    if user_input == "0000":
        print("You have unlocked the software.")
    else:
        quit()
        """
logs = open("intrusion_log.txt", "w")
logs.write("")
print("__Welcome to Z_CRYPT 2.0 !__\nA cryptography software.\nEvery user has a unique crypting key, which means that you can only open your own files!")

user_input = input("Do you have an account ? (y/n) : ")                 #On demande a l'utilisateur s'il dispose d'un compte
if user_input == 'n':
    user_input = input("Do you want to create one ? (y/n) : ")          #S'il n'en a pas on lui propose d'en créer un
    if user_input == 'y':
        user_input = 0
        while user_input == 0:                                          #Tant que le return de la fonction de creation de compte est égal a 0 on reste dans la boucle
            user_login = input("Enter a new login : ")                  #On demande a l'utilisation de saisir un login
            user_password = input("Enter a new password : ")            #On demande a l'utilisation de saisir un mot de passe
            user_input = account_creation(user_login, user_password)    #On rentre dans la fonction de création de compte contenue dans le module utils.py
    else:
        print("Thank you for using Z_Crypt 2.0 !")
        logs = open("logs.txt", "a")
        logs.write("\n[" + str(now.strftime("%d/%m/%Y %H:%M:%S")) + "]" + "- An unknown user has exited the software")
        logs.close()
        quit()                                                          #Si l'utilisateur ne veut pas se créer de compte on quitte le programme
else:                                                                   #Si l'utilisateur a déjà un compte on passe a la suite
    pass

while login_success == False and user_try > 0:
    logs = open("logs.txt", "a")
    user_login = input("Enter your login : ")
    user_password = input("Enter your password : ")

    login_input = user_login + ":" + user_password

    auth_file = open("auth.txt", "r")
    auth_file = auth_file.read()

    if auth_file.find(login_input) != -1 and len(login_input) > 1:
        login_success = True
        logs.write("\n[" + str(now.strftime("%d/%m/%Y %H:%M:%S")) + "]- " + user_login + " succesfully loged in")
    elif login_success == False and user_try > 0:
        logs.write("\n[" + str(now.strftime("%d/%m/%Y %H:%M:%S")) + "]" + "- A user failed to log in")
        user_try -= 1
        print("Wrong login or password !\n" + str(user_try) + " try left before auto-destruction!")
        login_success = False
    if login_success == False and user_try < 1:
        send_mail.sendmail()
        print("An email has been sent to the owner.\nu15sm1982748wmq.13 exit code.")
        logs.write("\n[" + str(now.strftime("%d/%m/%Y %H:%M:%S")) + "]" + "- A user failed to log in")
        logs.close()
        local_ip = socket.gethostbyname('localhost')
        logs = open("intrusion_log.txt", "w")
        logs.write("\n[" + str(now.strftime("%d/%m/%Y %H:%M:%S")) + "]" + "- AN INTRUDER HAS BEEN DETECTED\n"
                                                                          "Someone tried to access the software and"
                                                                          " failed 5 times\nto enter a valid login and"
                                                                          " password combination\nIP Adress : " + local_ip + "\n")
        logs.close()
        quit()

if login_success == True:
    key = key_parser("auth.txt", login_input)
    print("Welcome " + user_login + "!\nYour encryption key is : " + str(key))

while login_success == True:
    extension = ".txt"
    file_path = "./files/"

    user_input = input("What would you like to do ? (read/write/append/encrypt/decrypt/remove/quit) : \n")

    if user_input != "quit":
        name = input("Which file would you like to modify ? (only type the filename without the path and the extension)\n")
        name = file_path + name + extension
        if path.exists(name):
            pass
        else:
            user_input = input("The filename specified does not exist yet. Would you like to create it ? (y/n) \n")
            if user_input == "y":
                user_input = "write"
            else:
                user_input = None

    if user_input == "encrypt":
        f = open(name, "a")
        f = read_file(name, f)
        print("Decrypted text : " + f)
        f = encryption(name, f, key)
        f = open(name, "r")
        f = read_file(name, f)
        print("Encrypted text : " + f)
        logs.write("\n[" + str(now.strftime("%d/%m/%Y %H:%M:%S")) + "]- " + name + " has been encrypted by " + user_login + ".")
    elif user_input == "write":
            f = open(name, "w")
            user_input = input("You can write in the file. ")
            f.write(user_input)
            logs.write("\n[" + str(
            now.strftime("%d/%m/%Y %H:%M:%S")) + "]- " + name + " has been created by " + user_login + ".")
    elif user_input == "append":
        f = open(name, "a")
        user_input = input("You can write in the file. ")
        f.write(user_input)
        logs.write("\n[" + str(now.strftime("%d/%m/%Y %H:%M:%S")) + "]- " + name + " has been modified by " + user_login + ".")
    elif user_input == "decrypt":
        f = open(name, "a")
        f = read_file(name, f)
        print("Encrypted text : " + f)
        f = decryption(name, f, key)
        f = open(name, "r")
        f = read_file(name, f)
        print("Decrypted text : " + f)
        logs.write("\n[" + str(now.strftime("%d/%m/%Y %H:%M:%S")) + "]- " + name + " has been decrypted by " + user_login + ".")
    elif user_input == "remove":
        logs.write("\n[" + str(now.strftime("%d/%m/%Y %H:%M:%S")) + "]- " + name + " has been deleted by " + user_login + ".")
        delete_file(name)
    elif user_input == "read":
        f = open(name, "r")
        logs.write("\n[" + str(now.strftime("%d/%m/%Y %H:%M:%S")) + "]- " + name + " has been read by " + user_login + ".")
        print(f.read())
    elif user_input == "quit":
        user_input = input("Are you sure that you want to quit ? (y/n) ")
        if user_input == "y":
            login_success = False
            logs.write("\n[" + str(now.strftime("%d/%m/%Y %H:%M:%S")) + "]- " + user_login + " has been disconnected.")
            print("Thank you for using Z_Crypt 2.0 !")
        elif user_login == "root" and user_input == "logs":
            f = open("./logs.txt", "r")
            print(f.read())
        elif user_login == "root" and user_input == "auth":
            f = open("./auth.txt", "r")
            print(f.read())
        else:
            user_input = None
