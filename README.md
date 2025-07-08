
# Projet MongoDB RH – Master Big Data & IA

**Projet de fin de module** – Bases de Données NoSQL  
**Thème :** Conception d’un système RH complet avec MongoDB  
**Langage :** Python (PyMongo)  
**Binôme :** Essodolom BOUWEKA & Et Johnson Daniel

---

## 🎯 Objectif

Ce projet a pour but de concevoir et exploiter un **système d'information RH** complet avec **MongoDB** en utilisant le pilote **PyMongo**.  
Il répond aux exigences du module de base de données NoSQL avec :

- 3 collections relationnelles (employés, postes, départements)
- Embedding et referencing
- Jeu de données réaliste (20+ documents/collection)
- 20 requêtes documentées
- Utilisation de MongoDB Atlas (bonus)
- Gestion des accès utilisateurs (sécurité)

---

##  Architecture du projet
Le projet est structuré de manière modulaire pour faciliter la maintenance et l'évolution. Voici l'architecture du projet :

```
Projet_MongoDB_RH/
  data/
    employes.json
    postes.json
    departements.json
  scripts/
    insert_data.py
    create_user.py
  queries/
    crud_queries.py
    advanced_queries.py
    aggregation_queries.py
  main.py
  .env
  .gitignore
  requirements.txt
  README.md




## Installation et exécution
1. Cloner le dépôt  
git clone https://github.com/EssodolomBouweka/mongodb-rh.git
cd projet-mongodb-rh


2. Créer un environnement virtuel (optionnel)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows


3. Installer les dépendances
pip install -r requirements.txt

4. Créer l'utilisateur MongoDB (optionnel)
python scripts/create_user.py

5. configure l'environnement MongoDB dans `.env` :
```MONGO_URI=mongodb://localhost:27017
DB_NAME=entreprise_rh

6. insert les données
python scripts/insert_data.py


7. Exécuter les requêtes
python queries/crud_queries.py





