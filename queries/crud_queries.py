from utils.db_connection import db
from bson.objectid import ObjectId

# --- Fonctions CRUD pour les employés ---

def ajouter_employe(nom, email, poste_id, dept_id, competences, contrat):
    """
    Ajoute un nouvel employé dans la collection 'employes'.
    poste_id et dept_id doivent être des chaînes hexadécimales valides d'ObjectId.
    contrat est un dictionnaire avec les clés : type, salaire, date_debut.
    """
    employe = {
        "nom": nom,
        "email": email,
        "date_embauche": contrat.get("date_debut", "2024-01-01"),
        "poste_id": ObjectId(poste_id),
        "departement_id": ObjectId(dept_id),
        "competences": competences,
        "contrat": contrat
    }
    db.employes.insert_one(employe)

def lister_employes():
    """
    Retourne un curseur MongoDB sur tous les employés.
    """
    return db.employes.find()

def trouver_employe_par_email(email):
    """
    Cherche un employé par son email et retourne un seul document.
    """
    return db.employes.find_one({"email": email})

def maj_salaire(email, nouveau_salaire):
    """
    Met à jour le salaire dans le contrat d’un employé identifié par email.
    """
    db.employes.update_one(
        {"email": email},
        {"$set": {"contrat.salaire": nouveau_salaire}}
    )

def supprimer_employe(email):
    """
    Supprime un employé identifié par email.
    """
    db.employes.delete_one({"email": email})

def ajouter_competence(email, competence):
    """
    Ajoute une compétence à la liste des compétences d’un employé.
    """
    db.employes.update_one(
        {"email": email},
        {"$push": {"competences": competence}}
    )

def retirer_competence(email, competence):
    """
    Supprime une compétence de la liste des compétences d’un employé.
    """
    db.employes.update_one(
        {"email": email},
        {"$pull": {"competences": competence}}
    )

# --- Fonctions CRUD pour les départements ---

def ajouter_departement(nom, description, budget, date_creation="2023-01-01"):
    """
    Ajoute un nouveau département avec son budget et date de création.
    """
    db.departements.insert_one({
        "nom": nom,
        "description": description,
        "budget": budget,
        "date_creation": date_creation
    })

def lister_departements():
    """
    Retourne un curseur sur tous les départements.
    """
    return db.departements.find()

def trouver_departement_par_nom(nom):
    """
    Trouve un département par son nom.
    """
    return db.departements.find_one({"nom": nom})

def maj_budget_departement(nom, nouveau_budget):
    """
    Met à jour le budget d’un département identifié par son nom.
    """
    db.departements.update_one(
        {"nom": nom},
        {"$set": {"budget": nouveau_budget}}
    )

def supprimer_departement(nom):
    """
    Supprime un département par son nom.
    """
    db.departements.delete_one({"nom": nom})

# --- Fonctions CRUD pour les postes ---

def ajouter_poste(titre, description, niveau, date_creation="2023-01-01"):
    """
    Ajoute un nouveau poste avec titre, description, niveau d'expérience et date de création.
    """
    db.postes.insert_one({
        "titre": titre,
        "description": description,
        "niveau_experience": niveau,
        "date_creation": date_creation
    })

def lister_postes():
    """
    Retourne un curseur sur tous les postes.
    """
    return db.postes.find()

def trouver_poste_par_titre(titre):
    """
    Trouve un poste par son titre.
    """
    return db.postes.find_one({"titre": titre})

def maj_description_poste(titre, nouvelle_description):
    """
    Met à jour la description d’un poste identifié par son titre.
    """
    db.postes.update_one(
        {"titre": titre},
        {"$set": {"description": nouvelle_description}}
    )

def supprimer_poste(titre):
    """
    Supprime un poste par son titre.
    """
    db.postes.delete_one({"titre": titre})


# --- Exemple simple d'utilisation ---
if __name__ == "__main__":
    print("📄 Liste de tous les employés :")
    for emp in lister_employes():
        print(emp["nom"], "-", emp["email"])

    print("\n🔍 Recherche d’un département nommé 'Marketing' :")
    dep = trouver_departement_par_nom("Marketing")
    print(dep)
    if dep:
        print("Département trouvé :", dep["nom"])
    else:
        print("Aucun département trouvé.")
        