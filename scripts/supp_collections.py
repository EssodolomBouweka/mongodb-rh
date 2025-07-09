import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Charger .env
load_dotenv()

# Connexion Mongo
MONGO_MODE = os.getenv("MONGO_MODE", "local")
MONGO_URI = os.getenv("MONGO_ATLAS_URI") if MONGO_MODE == "atlas" else os.getenv("MONGO_LOCAL_URI")
DB_NAME = os.getenv("DB_NAME", "rh_management")
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Liste des collections à supprimer
collections_to_drop = ['departements', 'postes', 'employes']

for coll_name in collections_to_drop:
    if coll_name in db.list_collection_names():
        db[coll_name].drop()
        print(f"✅ Collection '{coll_name}' supprimée.")
    else:
        print(f"⚠️ Collection '{coll_name}' n'existe pas.")
