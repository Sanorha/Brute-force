# 🔐 Brute Force V1 - Recherche de mot de passe

## 🧠 Pourquoi ce projet ?

Ce projet permet d'illustrer la méthode de brute force pour trouver un mot de passe. Il commence par chercher chaque caractère du mot de passe, un par un, en commençant par le premier, puis le deuxième, et ainsi de suite jusqu'à ce que le mot de passe soit entièrement trouvé. Chaque essai est un caractère généré aléatoirement, qui est comparé au caractère correspondant du mot de passe cible. Cette approche permet de visualiser la lenteur et la méthode utilisée dans les attaques par brute force.

## 📝 Fonctionnalités

- Le programme demande à l'utilisateur de saisir le mot de passe à trouver.
- Le script génère des caractères aléatoires et les compare un par un avec chaque caractère du mot de passe jusqu'à ce qu'il soit entièrement trouvé.
- L'efficacité de l'attaque brute force est mesurée par le temps nécessaire pour trouver le mot de passe.

## ▶️ Exemple d'utilisation

```bash
$ python3 brute_force_V1.py
```
Quel est le mot de passe : test123  
Mot trouvé : test123  
Durée : 4.56 secondes  

## ⚠️ Avertissement

> Ce script est **strictement éducatif**. Il ne doit en aucun cas être utilisé pour tenter de déchiffrer des mots de passe réels ou accéder à des systèmes sans autorisation.

---

📁 Projet réalisé dans le cadre de ma candidature à une formation en cybersécurité.  
