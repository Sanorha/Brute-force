# 🔐 Brute Force V2 - Recherche de mot de passe par hash (MD5)

## 🧠 Pourquoi ce projet ?
Ce projet permet d'illustrer une attaque par brute force visant à casser un mot de passe hashé en MD5. L'utilisateur entre un mot de passe dont le hash MD5 est calculé. Ensuite, le programme tente de trouver ce hash parmi une liste de mots (dictionnaire) et de les comparer jusqu'à ce qu'il trouve la correspondance. Cette méthode permet de visualiser l'efficacité d'un dictionnaire dans une attaque par force brute contre les mots de passe.

## 📝 Fonctionnalités
- Le programme demande à l'utilisateur de saisir un mot de passe, puis il calcule son hash MD5.
- Il compare ce hash avec les hash MD5 des mots d'un fichier dictionnaire.
- Si une correspondance est trouvée, le mot de passe est affiché avec son hash MD5.
- Le temps nécessaire pour casser le mot de passe est également mesuré.

## ▶️ Exemple d'utilisation
```bash
$ python3 brute_force_V2.py
```
Quel est le mot de passe à deviner : abandon
b0bbb2218aa3c78802a8ed8c78aa2cae
Mot de passe trouvé : abandon (b0bbb2218aa3c78802a8ed8c78aa2cae) 
Durée : 3.24 secondes  

## ⚠️ Avertissement

> Ce script est **strictement éducatif**. Il ne doit en aucun cas être utilisé pour tenter de déchiffrer des mots de passe réels ou accéder à des systèmes sans autorisation.

---

📁 Projet réalisé dans le cadre de ma candidature à une formation en cybersécurité.  
