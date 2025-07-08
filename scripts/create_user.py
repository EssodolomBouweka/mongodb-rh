from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
admin = MongoClient(os.getenv("MONGO_URI"))
db = admin[os.getenv("DB_NAME")]

try:
    db.command("createUser", "stagiaire",
               pwd="stagiaire123",
               roles=[{"role": "readWrite", "db": os.getenv("DB_NAME")}])
    print("Utilisateur 'stagiaire' créé avec succès.")
except Exception as e:
    print("Erreur :", e)
