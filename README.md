# Décodeur de Phrases

Ce projet Python permet de décoder des phrases chiffrées à l'aide d'un dictionnaire de mots, avec une interface graphique simple pour tester le décodage. Il inclut également des outils pour importer et organiser des données textuelles.

## Structure du projet

- `decodeur.py` : Module principal pour le décodage, la gestion des données et l'interface graphique.
- `Data_up.py` : Script pour importer et formater des textes afin d'alimenter la base de données de mots.
- `test.py` : Exemple de chiffrement de texte (chiffre de César).
- `Data/` : Dossier contenant les fichiers de mots triés par longueur.
- `In/` : Dossier pour placer les fichiers à décoder (ex : `code1.txt`).
- `donne.txt` : Exemple de texte source pour alimenter la base de données.

## Fonctionnalités

- **Décodage automatique** de phrases chiffrées à partir de fichiers texte.
- **Gestion d'une base de données** de mots, triés par longueur, pour faciliter le décodage.
- **Interface graphique** simple (Tkinter) pour tester le décodage de phrases.
- **Importation et nettoyage** de textes pour enrichir la base de données de mots.

## Utilisation

1. **Importer des mots dans la base de données**  
   Lancer `Data_up.py` et fournir le chemin d'un fichier texte (ex : `donne.txt`).  
   Les mots seront extraits, nettoyés et ajoutés dans le dossier `Data/`.

2. **Placer un code à décoder**  
   Mettre un fichier texte à décoder dans le dossier `In/` (ex : `code1.txt`).

3. **Lancer le décodeur**  
   Exécuter `decodeur.py`. Le programme va lire les fichiers du dossier `In/` et tenter de décoder les phrases à l'aide de la base de données de mots.

4. **Utiliser l'interface graphique**  
   Lancer `decodeur.py` pour accéder à une interface simple permettant de tester le décodage de phrases.

## Dépendances

- Python 3.x
- Tkinter (inclus dans la plupart des distributions Python)
