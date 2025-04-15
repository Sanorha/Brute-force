#!/usr/bin/env python3
# coding:utf-8

import random
import time

# Demande le mot de passe à trouver
mot_de_passe = input("Quel est le mot de passe : ")

# Crée une liste de caractères en s'assurant que tous les caractères du mot de passe sont présents
lettres = list(set(mot_de_passe)) + list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#&()-_=+€éèàç ")

def mot_aleatoire():
    resultat = ""
    for i in range(len(mot_de_passe)):
        while True:
            c = random.choice(lettres)
            print(resultat + c)
            if c == mot_de_passe[i]:
                resultat += c
                break
    return resultat

debut = time.time()
mot_trouve = mot_aleatoire()
print("Mot trouvé :", mot_trouve)
print("Durée : {:.2f} secondes".format(time.time() - debut))
