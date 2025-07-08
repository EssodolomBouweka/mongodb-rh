from utils.db_connection import db
from bson.objectid import ObjectId

def salaire_moyen_par_contrat():
    """
    Calcule le salaire moyen pour chaque type de contrat (CDI, CDD, etc.).
    Retourne un curseur MongoDB avec le type de contrat et salaire moyen.
    """
    return db.employes.aggregate([
        { "$group": {
            "_id": "$contrat.type",
            "salaire_moyen": { "$avg": "$contrat.salaire" }
        }}
    ])

def nb_employes_par_departement_avec_nom():
    """
    Compte le nombre d’employés par département.
    Effectue une jointure ($lookup) pour récupérer le nom du département.
    Retourne un curseur avec nom du département et nombre d'employés.
    """
    return db.employes.aggregate([
        { "$group": {
            "_id": "$departement_id",
            "nombre_employes": { "$sum": 1 }
        }},
        { "$lookup": {
            "from": "departements",
            "localField": "_id",
            "foreignField": "_id",
            "as": "departement_info"
        }},
        { "$unwind": "$departement_info" },
        { "$project": {
            "departement_nom": "$departement_info.nom",
            "nombre_employes": 1
        }}
    ])

def nb_employes_par_departement():
    """
    Compte simplement le nombre d’employés par département (sans jointure).
    """
    return db.employes.aggregate([
        { "$group": {
            "_id": "$departement_id",
            "nb_employes": { "$sum": 1 }
        }}
    ])

def employes_avec_infos_poste():
    """
    Liste les employés avec les informations complètes de leur poste.
    Utilise $lookup pour joindre la collection postes.
    """
    return db.employes.aggregate([
        { "$lookup": {
            "from": "postes",
            "localField": "poste_id",
            "foreignField": "_id",
            "as": "poste"
        }},
        { "$unwind": "$poste" }
    ])

def employes_avec_infos_departement():
    """
    Liste les employés avec les infos complètes de leur département.
    Utilise $lookup pour joindre la collection departements.
    """
    return db.employes.aggregate([
        { "$lookup": {
            "from": "departements",
            "localField": "departement_id",
            "foreignField": "_id",
            "as": "departement"
        }},
        { "$unwind": "$departement" }
    ])

def top_5_salaires():
    """
    Affiche les 5 employés ayant les salaires les plus élevés.
    Trie par salaire décroissant, limite à 5, puis affiche nom, email, salaire.
    """
    return db.employes.aggregate([
        { "$sort": { "contrat.salaire": -1 } },
        { "$limit": 5 },
        { "$project": {
            "nom": 1,
            "email": 1,
            "salaire": "$contrat.salaire"
        }}
    ])

def nb_employes_par_competence():
    """
    Compte combien d'employés possèdent chaque compétence.
    $unwind décompose la liste des compétences pour le groupement.
    """
    return db.employes.aggregate([
        { "$unwind": "$competences" },
        { "$group": {
            "_id": "$competences",
            "nb": { "$sum": 1 }
        }},
        { "$sort": { "nb": -1 } }
    ])

def employes_apres_2023():
    """
    Liste les employés embauchés après le 1er janvier 2023.
    Retourne nom, email, date d’embauche.
    """
    return db.employes.aggregate([
        { "$match": { "date_embauche": { "$gte": "2023-01-01" } } },
        { "$project": {
            "nom": 1,
            "email": 1,
            "date_embauche": 1
        }}
    ])

def salaire_moyen_par_poste():
    """
    Calcule la moyenne des salaires pour chaque poste (groupé par poste_id).
    """
    return db.employes.aggregate([
        { "$group": {
            "_id": "$poste_id",
            "salaire_moyen": { "$avg": "$contrat.salaire" }
        }}
    ])

def employes_plus_de_3_competences():
    """
    Liste les employés ayant plus de 3 compétences.
    Utilise $project pour compter le nombre de compétences,
    puis $match pour filtrer ceux avec plus de 3.
    """
    return db.employes.aggregate([
        { "$project": {
            "nom": 1,
            "email": 1,
            "nombre_competences": { "$size": "$competences" }
        }},
        { "$match": {
            "nombre_competences": { "$gt": 3 }
        }}
    ])


# Exemple de test
if __name__ == "__main__":
    print("--- Salaire moyen par type de contrat ---")
    for res in salaire_moyen_par_contrat():
        print(res)

    print("\n--- Employés avec plus de 3 compétences ---")
    for emp in employes_plus_de_3_competences():
        print(f"{emp['nom']} - {emp['email']} - compétences : {emp['nombre_competences']}")
