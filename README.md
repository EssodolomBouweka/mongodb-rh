
# Projet MongoDB RH – Master Big Data & IA

**Projet de fin de module** – Bases de Données NoSQL  
**Thème :** Conception d’un système RH complet avec MongoDB  
**Langage :** Python (PyMongo)  
**Binôme :** Essodolom BOUWEKA & Et DJONSOHN Daniel

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

Le projet est structuré comme suit :

Projet_MongoDB_RH/
├── data/ # Données JSON
│ ├── employes.json
│ ├── postes.json
│ └── departements.json
│
├── scripts/ # Scripts techniques
│ ├── insert_data.py # Insertion des données
│ └── create_user.py # Création d'un utilisateur MongoDB
│
├── queries/ # Requêtes MongoDB
│ ├── crud_queries.py
│ ├── advanced_queries.py
│ └── aggregation_queries.py
│
├── main.py # Interface console du système RH
├── .env # Configuration MongoDB (locale ou Atlas)
├── .gitignore # Fichier d'exclusion Git
├── requirements.txt # Dépendances Python
└── README.md # Ce fichier



## Installation et exécution
1. Cloner le dépôt  
git clone https://github.com/votre-utilisateur/projet-mongodb-rh.git
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





