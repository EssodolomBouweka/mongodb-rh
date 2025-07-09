# db_connection.py

import os
from dotenv import load_dotenv
from pymongo import MongoClient, errors

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer le mode de connexion : "local" ou "atlas"
MONGO_MODE = os.getenv("MONGO_MODE", "local")

# Choisir l'URI en fonction du mode
if MONGO_MODE == "atlas":
    MONGO_URI = os.getenv("MONGO_ATLAS_URI")
else:
    MONGO_URI = os.getenv("mongodb://localhost:27017")

# Récupérer le nom de la base
DB_NAME = os.getenv("rh_management", "rh_management")

# Vérifier que les variables d'environnement critiques sont bien définies
if not MONGO_URI or not DB_NAME:
    raise ValueError("❌ MONGO_URI ou DB_NAME est manquant dans le fichier .env.")

# Connexion à MongoDB
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)  # timeout 5s
    client.server_info()  # force la connexion pour détecter les erreurs tôt
    db = client[DB_NAME]
    print(f"✅ Connexion à MongoDB ({MONGO_MODE}) réussie. Base : {DB_NAME}")
except errors.ServerSelectionTimeoutError as err:
    raise ConnectionError(f"❌ Échec de la connexion à MongoDB : {err}")
