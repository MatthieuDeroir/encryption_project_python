from keys import *


def account_creation(login, password):  # fonction de creation de compte
    login_input = login + ":" + password
    auth_file = open("auth.txt", "r")
    auth = auth_file.read()  # On ouvre le fichier qui contient tout les login, mdp et key des utilisateurs
    if auth.find(login_input) != -1:  # On teste si le compte n'existe pas déjà
        print("The login already exist, please retry.")
        return 0
    elif len(login) > 6 or len(login) <= 0 or len(password) > 6 or len(password) <= 0:  # On ne veut pas que ni le login ni le mdp n'excede 6 caracteres et qu'ils soient vide
        print("Your login and password size must be between 1 and 6 characters !")
        return 0
    else:
        auth_file = open("auth.txt", "a")  # Si toutes les conditions sont respectees
        login_input = login + ":" + password
        key = key_generator(login_input)  # On recupere une clef a partir de la suite constitutive du login
        auth_file.write("\n" + login_input + "=" + str(key))  # On ecrit les informations de connexions dans le fichier
        print("Account successfully created !\nYou can log in now.")
    return 1
