
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
import csv

load_dotenv()

# Connexion à MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

def afficher_menu():
    print("\n=== MENU RH MongoDB ===")
    print("1. Afficher tous les employés")
    print("2. Ajouter un nouvel employé (test)")
    print("3. Rechercher un employé par email")
    print("4. Supprimer un employé")
    print("5. Afficher les top 5 salaires")
    print("6. Filtrer les employés par département")
    print("7. Lister les compétences dans l’entreprise")
    print("8. Nombre d’employés par contrat")
    print("9. Exporter les employés en CSV")
    print("0. Quitter")

def afficher_employes():
    print("\n--- Liste des employés ---")
    for emp in db.employes.find():
        print(f"{emp.get('nom')} - {emp.get('email')} - {emp['contrat']['salaire']} F")

def ajouter_employe():
    print("\n--- Ajouter un employé (test) ---")
    nom = input("Nom : ")
    email = input("Email : ")
    salaire = int(input("Salaire : "))
    poste_id = db.postes.find_one({}, {"_id": 1})["_id"]
    dept_id = db.departements.find_one({}, {"_id": 1})["_id"]

    employe = {
        "nom": nom,
        "email": email,
        "date_embauche": "2024-06-01",
        "poste_id": poste_id,
        "departement_id": dept_id,
        "competences": ["Test", "MongoDB"],
        "contrat": {
            "type": "CDI",
            "salaire": salaire,
            "date_debut": "2024-06-01"
        }
    }
    db.employes.insert_one(employe)
    print("✅ Employé ajouté avec succès.")

def rechercher_par_email():
    email = input("\nEntrez l'email de l'employé : ")
    emp = db.employes.find_one({"email": email})
    if emp:
        print(f"Nom : {emp['nom']}")
        print(f"Email : {emp['email']}")
        print(f"Salaire : {emp['contrat']['salaire']}")
    else:
        print("❌ Aucun employé trouvé.")

def supprimer_employe():
    email = input("\nEmail de l'employé à supprimer : ")
    result = db.employes.delete_one({"email": email})
    if result.deleted_count > 0:
        print("✅ Employé supprimé.")
    else:
        print("❌ Aucun employé trouvé.")

def top_5_salaires():
    print("\n--- Top 5 des salaires ---")
    top = db.employes.aggregate([
        {"$sort": {"contrat.salaire": -1}},
        {"$limit": 5},
        {"$project": {"nom": 1, "email": 1, "contrat.salaire": 1}}
    ])
    for emp in top:
        print(f"{emp['nom']} - {emp['email']} - {emp['contrat']['salaire']} F")

def filtrer_par_departement():
    nom_dept = input("Nom du département : ")
    dept = db.departements.find_one({"nom": nom_dept})
    if not dept:
        print("❌ Département introuvable.")
        return
    emp_list = db.employes.find({"departement_id": dept["_id"]})
    print(f"\n--- Employés du département {nom_dept} ---")
    for emp in emp_list:
        print(f"{emp['nom']} - {emp['email']}")

def lister_competences_uniques():
    result = db.employes.aggregate([
        {"$unwind": "$competences"},
        {"$group": {"_id": "$competences"}},
        {"$sort": {"_id": 1}}
    ])
    print("\n--- Compétences dans l’entreprise ---")
    for comp in result:
        print(f"- {comp['_id']}")

def nb_employes_par_contrat():
    stats = db.employes.aggregate([
        {"$group": {"_id": "$contrat.type", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}}
    ])
    print("\n--- Nombre d’employés par contrat ---")
    for stat in stats:
        print(f"{stat['_id']} : {stat['total']}")

def exporter_employes_csv():
    emp_list = db.employes.find()
    with open("employes_export.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nom", "Email", "Salaire", "Type de contrat"])
        for emp in emp_list:
            writer.writerow([
                emp["nom"],
                emp["email"],
                emp["contrat"]["salaire"],
                emp["contrat"]["type"]
            ])
    print("✅ Fichier employes_export.csv généré avec succès.")

# Lancement du menu
if __name__ == "__main__":
    while True:
        afficher_menu()
        choix = input("Choix : ")
        if choix == "1":
            afficher_employes()
        elif choix == "2":
            ajouter_employe()
        elif choix == "3":
            rechercher_par_email()
        elif choix == "4":
            supprimer_employe()
        elif choix == "5":
            top_5_salaires()
        elif choix == "6":
            filtrer_par_departement()
        elif choix == "7":
            lister_competences_uniques()
        elif choix == "8":
            nb_employes_par_contrat()
        elif choix == "9":
            exporter_employes_csv()
        elif choix == "0":
            print("Au revoir 👋")
            break
        else:
            print("⛔ Choix invalide.")
