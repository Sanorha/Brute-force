# 🔐 Brute Force sur Mot de Passe – Projet Python

Ce projet est une démonstration éducative d'une attaque **brute-force** réalisée en Python. Il s'agit d'un script simple qui tente de deviner un mot de passe, caractère par caractère, en utilisant une approche aléatoire.

## 🎯 Objectif

Ce script a été conçu dans un cadre **pédagogique** pour illustrer :
- le fonctionnement basique d'une attaque par force brute ;
- la gestion de l'encodage et des caractères spéciaux (comme `é`, `€`, etc.) en Python ;
- la mise en pratique de concepts simples de programmation : boucles, gestion du temps, chaînes de caractères, import de modules, etc.

---

## 💡 Fonctionnement

- Le script demande à l'utilisateur de saisir un mot de passe.
- Il tente ensuite de le retrouver **lettre par lettre** en comparant chaque caractère généré aléatoirement avec celui du mot de passe.
- Il affiche chaque tentative intermédiaire.
- À la fin, il affiche le mot trouvé ainsi que le **temps nécessaire pour y parvenir**.

---

## 🧪 Exemple d'utilisation

$ python3 brute_force.py
Quel est le mot de passe : Café€


C
Ca
Caf
Café
Café€
Mot trouvé : Café€
Durée : 4.12 secondes

## 🧠 Pourquoi ce projet ?

En cybersécurité, il est crucial de comprendre les bases des attaques, même les plus simples. Ce projet montre concrètement :

- la lenteur du brute-force sans optimisation,
- l’importance de la complexité des mots de passe,
- les limites de l’approche naïve.

Il s'agit d’un **projet d’initiation**, qui pourrait être ensuite enrichi (multithreading, dictionnaires, stats, etc.).

## ⚠️ Avertissement

> Ce script est **strictement éducatif**. Il ne doit en aucun cas être utilisé pour tenter de déchiffrer des mots de passe réels ou accéder à des systèmes sans autorisation.

---

📁 Projet réalisé dans le cadre de ma candidature à une formation en cybersécurité.  
