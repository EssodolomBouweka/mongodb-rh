from utils.db_connection import db
from bson.objectid import ObjectId

def liste_employes_competence_mongodb():
    """
    Liste tous les employés qui ont "MongoDB" dans leurs compétences.
    """
    return db.employes.find({"competences": "MongoDB"})

def employes_salaire_superieur_a(valeur=500000):
    """
    Trouve les employés dont le salaire est supérieur à une valeur donnée (500000 par défaut).
    """
    return db.employes.find({"contrat.salaire": {"$gt": valeur}})

def employes_contrat_type(type_contrat="CDI"):
    """
    Trouve les employés dont le type de contrat correspond au type donné (CDI par défaut).
    """
    return db.employes.find({"contrat.type": type_contrat})

def employes_nom_commence_par_lettre(lettre="A"):
    """
    Trouve les employés dont le nom commence par la lettre donnée (A par défaut).
    """
    return db.employes.find({"nom": {"$regex": f"^{lettre}"}})

def employes_nom_contient_texte(texte="Edem"):
    """
    Trouve les employés dont le nom contient un texte spécifique (ex: 'Edem').
    """
    return db.employes.find({"nom": {"$regex": texte}})

def employes_embauche_apres(date="2023-01-01"):
    """
    Trouve les employés embauchés après une date donnée (format 'YYYY-MM-DD').
    """
    return db.employes.find({"date_embauche": {"$gt": date}})

def employes_par_departement(departement_id):
    """
    Trouve les employés appartenant à un département donné (ObjectId).
    """
    return db.employes.find({"departement_id": ObjectId(departement_id)})

def employes_plus_de_trois_competences():
    """
    Trouve les employés ayant plus de 3 compétences.
    ATTENTION : la requête initiale avec $size et $gt ne fonctionne pas directement,
    car $size ne supporte pas $gt. Utiliser une agrégation pour cela (voir aggregation_queries).
    """
    # Ici juste exemple avec $size égal à 4 (plus de 3)
    return db.employes.find({"competences": {"$size": 4}})

def employes_salaire_entre(min_sal=500000, max_sal=1000000):
    """
    Trouve les employés dont le salaire est entre min_sal et max_sal inclus.
    """
    return db.employes.find({
        "contrat.salaire": {
            "$gte": min_sal,
            "$lte": max_sal
        }
    })

def employes_nom_contient_ae():
    """
    Trouve les employés dont le nom contient 'a' ou 'e'.
    """
    return db.employes.find({"nom": {"$regex": "[ae]"}})

def employes_nom_sans_a():
    """
    Trouve les employés dont le nom ne contient pas 'a'.
    """
    return db.employes.find({"nom": {"$not": {"$regex": "a"}}})

def employes_nom_dans_liste(noms):
    """
    Trouve les employés dont le nom est dans une liste donnée.
    noms doit être une liste de chaînes, ex : ["Edem Kodjo", "Julien Ayayi"].
    """
    return db.employes.find({"nom": {"$in": noms}})

def liste_simplifiee_nom_email():
    """
    Retourne une liste simplifiée des employés avec uniquement nom et email (sans _id).
    """
    return db.employes.find({}, {"nom": 1, "email": 1, "_id": 0})

def employes_nom_commence_par_a_et_competence_mongodb():
    """
    Trouve les employés dont le nom commence par 'A' et qui ont 'MongoDB' dans leurs compétences.
    """
    return db.employes.find({
        "nom": {"$regex": "^A"},
        "competences": "MongoDB"
    })

def employes_avec_champ_competences():
    """
    Trouve tous les employés qui ont un champ 'competences'.
    """
    return db.employes.find({"competences": {"$exists": True}})

def employes_poste_dans_liste(ids_postes):
    """
    Trouve les employés qui occupent l’un des postes listés.
    ids_postes est une liste d’ObjectId.
    """
    return db.employes.find({
        "poste_id": {"$in": ids_postes}
    })

def employes_sans_competence():
    """
    Trouve les employés qui n’ont pas de champ 'competences'.
    """
    return db.employes.find({"competences": {"$exists": False}})

def employes_contrat_cdd_ou_cdi():
    """
    Trouve les employés dont le contrat est de type 'CDD' ou 'CDI'.
    """
    return db.employes.find({
        "contrat.type": {"$in": ["CDD", "CDI"]}
    })
