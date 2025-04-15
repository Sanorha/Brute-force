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

```bash
$ python3 brute_force.py
Quel est le mot de passe : Café€
C
Ca
Caf
Café
Café€
Mot trouvé : Café€
Durée : 4.12 secondes
