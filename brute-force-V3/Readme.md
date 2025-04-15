# 🔐 Brute Force V3 - Casseur de mot de passe MD5

## 🧠 Pourquoi ce projet ?
Ce projet permet de casser un mot de passe hashé en MD5 en utilisant plusieurs méthodes :
1. **Dictionnaire** : Chercher dans un fichier de mots-clés.
2. **Incrémental** : Essayer toutes les combinaisons possibles de lettres jusqu'à atteindre la longueur du mot de passe.
3. **En ligne** : Chercher le hash en ligne via Google.

Il permet d'illustrer différentes techniques utilisées pour attaquer un mot de passe hashé et montre comment une simple méthode peut être améliorée en termes d'efficacité en fonction du type de source utilisée (fichier, brut, en ligne).

## 📝 Fonctionnalités
- **Génération de hash MD5** : Génère un hash MD5 à partir d'un mot de passe donné.
- **Crack par dictionnaire** : Cherche une correspondance en utilisant un fichier de mots-clés.
- **Crack incrémental** : Génère toutes les combinaisons possibles de lettres pour un mot de passe d'une longueur spécifiée.
- **Crack en ligne** : Recherche le hash MD5 dans les résultats de recherche Google.

## ▶️ Utilisation
```bash
usage: script.py [-h] [-f FILE] [-g GEN] [-md5 MD5] [-l PLENGTH] [-o]

Casseur de mot de passe en Python

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Chemin du fichier de mots clés
  -g GEN, --gen GEN     Génère un hash MD5 du mot de passe donné
  -md5 MD5              Mot de passe MD5 à casser
  -l PLENGTH            Longueur du mot de passe (mode incrémental seulement)
  -o                    Cherche le hash en ligne (google)
```

## ⚠️ Avertissement

> Ce script est **strictement éducatif**. Il ne doit en aucun cas être utilisé pour tenter de déchiffrer des mots de passe réels ou accéder à des systèmes sans autorisation.

---

📁 Projet réalisé dans le cadre de ma candidature à une formation en cybersécurité.  
