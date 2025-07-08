from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

# Création explicite non nécessaire dans MongoDB, mais on peut créer un index
db.departements.create_index("nom", unique=True)
db.postes.create_index("intitule", unique=True)
db.employes.create_index("email", unique=True)

print("Collections initialisées avec indexes.")
