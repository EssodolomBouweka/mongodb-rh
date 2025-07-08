
from utils.db_connection import employees

// Ajouter un nouvel employé à la base RH.


db.employes.insert_one({
    "nom": "Edem Kodjo",
    "email": "edem.kodjo@entreprise.tg",
    "date_embauche": "2023-06-01",
    "poste_id": ObjectId("..."),
    "departement_id": ObjectId("..."),
    "competences": ["JavaScript", "React", "MongoDB"],
    "contrat": {
        "type": "CDI",
        "salaire": 750000,
        "date_debut": "2023-06-01"
    }
})

# Voir tous les employés de l’entreprise.

employes = db.employes.find()
for emp in employes:
    print(emp)

// Trouver l’employé ayant un certain email.

db.employes.find_one({"email": "essodolom.bouweka@entreprise.tg"})

// Mettre a jour le salaire dun employe

db.employes.update_one(
    {"email": "julien.ayayi@entreprise.tg"},
    {"$set": {"contrat.salaire": 900000}}
)
# Supprimer un employé de la base RH.
db.employes.delete_one({"email": "grace.akou@entreprise.tg"})

#Ajouter une compétence à un employé existant.

db.employes.update_one(
    {"email": "amivi.lawson@entreprise.tg"},
    {"$push": {"competences": "Gestion de projet"}}
)
# Supprimer une compétence d'un employé existant.   
db.employes.update_one(
    {"email": "amivi.lawson@entreprise.tg"},
    {"$pull": {"competences": "Gestion de projet"}}
)
# Ajouter un nouveau département à la base RH.
db.departements.insert_one({
    "nom": "Marketing",
    "description": "Département en charge des stratégies marketing et de la communication.",
    "budget": 5000000,
    "date_creation": "2023-01-01"
})
# Voir tous les départements de l’entreprise.
departements = db.departements.find()
for dep in departements:
    print(dep)
# Trouver un département par son nom.
db.departements.find_one({"nom": "Marketing"})
# Mettre à jour le budget d'un département.
db.departements.update_one(
    {"nom": "Marketing"},
    {"$set": {"budget": 6000000}}
)
# Supprimer un département de la base RH.
db.departements.delete_one({"nom": "Marketing"})
# Ajouter un nouveau poste à la base RH.
db.postes.insert_one({
    "titre": "Développeur Full Stack",
    "description": "Responsable du développement des applications web et mobiles.",
    "niveau_experience": "Intermédiaire",
    "date_creation": "2023-01-01"
})
# Voir tous les postes de l’entreprise.
postes = db.postes.find()
for poste in postes:
    print(poste)
    
    
# Trouver un poste par son titre.
db.postes.find_one({"titre": "Développeur Full Stack"})
# Mettre à jour la description d'un poste.
db.postes.update_one(
    {"titre": "Développeur Full Stack"},
    {"$set": {"description": "Responsable du développement des applications web et mobiles, avec une expertise en React et Node.js."}}
)


# Supprimer un poste de la base RH.
db.postes.delete_one({"titre": "Développeur Full Stack"})
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
import json
load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]



