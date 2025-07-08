
from utils.db_connection import employees
# Calculer le salaire moyen pour chaque type de contrat.

db.employes.aggregate([
    { "$group": {
        "_id": "$contrat.type",
        "salaire_moyen": { "$avg": "$contrat.salaire" }
    }}
])
# Calculer le nombre d'employés par département.    
db.employes.aggregate([
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
# Calculer le nombre d'employés par département deuxième manière
db.employes.aggregate([
    { "$group": {
        "_id": "$departement_id",
        "nb_employes": { "$sum": 1 }
    }}
])

 # Lister les employés avec les informations de leur poste (intitulé, salaire…).
 
 db.employes.aggregate([
    {
        "$lookup": {
            "from": "postes",
            "localField": "poste_id",
            "foreignField": "_id",
            "as": "poste"
        }
    },
    { "$unwind": "$poste" }
])
 
 #Lier chaque employé à son département (nom, chef…).

db.employes.aggregate([
    {
        "$lookup": {
            "from": "departements",
            "localField": "departement_id",
            "foreignField": "_id",
            "as": "departement"
        }
    },
    { "$unwind": "$departement" }
])

# Afficher les 5 salariés les mieux payés (nom, email, salaire).

 db.employes.aggregate([
    { "$sort": { "contrat.salaire": -1 } },
    { "$limit": 5 },
    { "$project": { "nom": 1, "email": 1, "contrat.salaire": 1 } }
])

# Compter combien d'employés possède chaque compétences
db.employes.aggregate([
    { "$unwind": "$competences" },
    { "$group": {
        "_id": "$competences",
        "nb": { "$sum": 1 }
    }},
    { "$sort": { "nb": -1 } }
])

#lister les employés recrutés après le 1er janvier 2023 (nom, email, date_embauche).

db.employes.aggregate([
    {
        "$match": {
            "date_embauche": { "$gte": "2023-01-01" }
        }
    },
    {
        "$project": {
            "nom": 1,
            "email": 1,
            "date_embauche": 1
        }
    }
])

# obtenir la moyenne des salaires par poste (poste_id, salaire_moyen).
db.employes.aggregate([
    { "$group": {
        "_id": "$poste_id",
        "salaire_moyen": { "$avg": "$contrat.salaire" }
    }}
])
# Lister les employés qui ont plus de 3 compétences (nom, email, nombre_competences).
db.employes.aggregate([
    {
        "$project": {
            "nom": 1,
            "email": 1,
            "nombre_competences": { "$size": "$competences" }
        }
    },
    {
        "$match": {
            "nombre_competences": { "$gt": 3 }
        }
    }
])

