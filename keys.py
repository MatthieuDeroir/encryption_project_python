import random

def key_generator(input): #Fonction de generation de clef a partir d'un input donné
    key = ""                #initialisation de la variable
    for c in str(input):        #On parcours l'input
        if c != ":" and len(key) < 4:   #on evite le : du login et on concatene tant que la taille de la clef n'excede pas 4
            key += str(ord(c))          #On concatene a la variable key chaque caractere qui aura prealablement ete convertit en ASCII grave à la fonction ord
            key = key.replace("1", "")      #On enleve tout les 1 (qui sont nombreux) ainsi que les 0
            key = key.replace("0", "")
        while len(key) < 4:
            key += str(random.randint(2, 9))
    while key_searcher(str(key)) != 1:  #On va chercher dans le fichier des infos de connexions si la clef n;existe pas déjà
        key = int(key)                  #Si elle existe on l'increment jusqu'a ce que l'on trouve une clef originale
        key += 1
        print(key)
    return (key)


def key_parser(file, login_input):       #C'est la fonction de parsing qui permet de recuperer la clef propre a chqaue utilisateur dans le fichier contenant les infos de connexion
    key = ""
    auth = open("auth.txt", "r")
    auth_str = auth.read()
    auth.close()
    index = auth_str.find(login_input + "=")    #On cherche dans le document la ligne ou se trouve la suite du login + le signe "=" qui precede le code et on recupere l'index
    key = auth_str[index+len(login_input) + 1:index+len(login_input) +5] #On copy dans une variable key a l'index donné auquel on rajoute la taille du login et du signe egal (+1) jusqu'a +4 (+5) car une clef ne fait que 4 chiffres
    return int(key)


def key_searcher(key):                      #c'est la fonction qui permet de chercher s'il y a une clef similaire dans le file descriptor donné
    auth = open("auth.txt", "r")
    auth_str = auth.read()
    auth.close()
    if auth_str.find(key) != -1:
        return 0
    return 1
