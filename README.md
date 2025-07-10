
# Projet MongoDB RH – Master Big Data & IA

## Contexte

Ce projet est réalisé dans le cadre du **projet de fin de module** du cours **Bases de Données NoSQL**.  
Il s'agit de concevoir et d'exploiter un **système d'information RH complet** basé sur **MongoDB**, en utilisant **PyMongo**.

---

## Réalisé par

- **Essodolom BOUWEKA**
- **Johnson Daniel**

---

## Objectifs pédagogiques

- Modéliser un système RH dans un environnement NoSQL
- Manipuler **3 collections** relationnelles :
  - `employes`
  - `postes`
  - `departements`
- Utiliser :
  - Le **data embedding**
  - Le **referencing** (`ObjectId`)
- Générer un **jeu de données réaliste** (+20 documents/collection)
- Implémenter au moins **20 requêtes** :
  - CRUD
  - Agrégations
  - Statistiques avancées
- (Bonus) Connexion via **MongoDB Atlas**
- (Bonus) **Gestion des utilisateurs MongoDB** via script sécurisé

---

## Architecture du projet

```
Projet_MongoDB_RH/
│
├── data/                    # Données JSON à importer
│   ├── employes.json
│   ├── postes.json
│   └── departements.json
│
├── scripts/                 # Scripts d'administration
│   ├── insert_data.py       → Injection des données
│   └── create_user.py       → Création d’un utilisateur MongoDB
│
├── queries/                 # Requêtes principales
│   ├── crud_queries.py      → Insert, update, delete, find
│   ├── advanced_queries.py  → Recherches avancées
│   └── aggregation_queries.py → Statistiques & agrégations
│
├── main.py                  # Script principal (optionnel) mais il est utilisable et il marche 
├── .env                     # Configuration MongoDB
├── .gitignore
├── requirements.txt         # Dépendances Python
└── README.md                # fichier de documentation du projet
```
Le dossier modelisation contient la modelisation de la base de données et un descriptif des choix de referencing ou de l'embedding 
---

## Installation et exécution

### 1. Cloner le dépôt

```bash
git clone https://github.com/EssodolomBouweka/mongodb-rh.git
cd mongodb-rh
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv venv
# Linux / macOS :
source venv/bin/activate
# Windows :
venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer la connexion MongoDB

Créez un fichier `.env` à la racine avec le contenu suivant :

```
MONGO_URI=mongodb://localhost:27017
DB_NAME=entreprise_rh
```

Si vous utilisez MongoDB Atlas, remplacez l’URI en conséquence.

---

## Utilisation

### 5. Créer un utilisateur MongoDB (optionnel)

```bash
python scripts/create_user.py
```

### 6. Insérer les données dans la base

```bash
python scripts/insert_data.py
```

### 7. Lancer les requêtes

```bash
# Requêtes CRUD de base
python queries/crud_queries.py

# Requêtes avancées
python queries/advanced_queries.py

# Requêtes d’agrégation
python queries/aggregation_queries.py
```

---

##  Requêtes intégrées

Plus de **20 requêtes** sont implémentées, incluant :

- Insertion et mise à jour des employés
- Filtrage par salaire, poste ou département
- Comptages, moyennes, regroupements (`$group`)
- Requêtes avec `$lookup`, `$match`, `$sort`, etc.

---

## Résultats attendus

- Une base RH remplie et structurée
- Des résultats d’analyse exploitables
- Une pratique concrète de MongoDB en environnement Python

---

## Licence

Projet académique – Master IA & Big Data  
Tous droits réservés © 2025
