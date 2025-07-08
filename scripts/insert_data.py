from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

# Chargement et insertion
def insert_json(file, collection):
    with open(file, encoding='utf-8') as f:
        data = json.load(f)
        result = db[collection].insert_many(data)
        print(f"Insertion dans {collection} : {len(result.inserted_ids)} documents.")

insert_json('data/departements.json', 'departements')
insert_json('data/postes.json', 'postes')
insert_json('data/employes.json', 'employes')
