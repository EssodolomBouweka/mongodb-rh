# db_connection.py

import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Choix du mode de connexion : local ou Atlas
MONGO_MODE = os.getenv("MONGO_MODE", "local")

if MONGO_MODE == "atlas":
    MONGO_URI = os.getenv("MONGO_ATLAS_URI")
else:
    MONGO_URI = os.getenv("MONGO_LOCAL_URI")

DB_NAME = os.getenv("DB_NAME")

# Vérification des variables essentielles
if not MONGO_URI or not DB_NAME:
    raise ValueError("❌ MONGO_URI ou DB_NAME est manquant dans le fichier .env")

# Connexion MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
