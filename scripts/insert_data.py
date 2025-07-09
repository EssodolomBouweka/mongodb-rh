import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

# Charger .env
load_dotenv()

# Déterminer la racine du projet (chemin absolu)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Connexion Mongo
MONGO_MODE = os.getenv("MONGO_MODE", "local")
MONGO_URI = os.getenv("MONGO_ATLAS_URI") if MONGO_MODE == "atlas" else os.getenv("MONGO_LOCAL_URI")
DB_NAME = os.getenv("DB_NAME", "rh_management")
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Fonction pour insérer un fichier JSON
def insert_json(filename, collection_name):
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        print(f"❌ Fichier non trouvé : {filepath}")
        return

    with open(filepath, encoding='utf-8') as f:
        data = json.load(f)
        if isinstance(data, list):
            result = db[collection_name].insert_many(data)
            print(f"✅ Insertion dans {collection_name} : {len(result.inserted_ids)} documents.")
        else:
            print(f"⚠️ Format invalide dans {filename} (doit être une liste JSON).")

# Insertion
insert_json('departements.json', 'departements')
insert_json('postes.json', 'postes')
insert_json('employes.json', 'employes')
