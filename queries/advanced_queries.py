from utils.db_connection import employees


#Lister tous les employés ayant “MongoDB” dans leurs compétences.

db.employes.find({"competences": "MongoDB"})

# Trouver les employés dont le salaire est supérieur à 500000.
db.employes.find({"contrat.salaire": {"$gt": 500000}})
# Trouver les employés dont le contrat est de type "CDI".
db.employes.find({"contrat.type": "CDI"})
# Trouver les employés dont le nom commence par "A".
db.employes.find({"nom": {"$regex": "^A"}})
# Trouver les employés dont le nom contient "Edem".
db.employes.find({"nom": {"$regex": "Edem"}})
# Trouver les employés embauchés après le 1er janvier 2023.
db.employes.find({"date_embauche": {"$gt": "2023-01-01"}})
# Trouver les employés appartenant à un département spécifique (par exemple, "Informatique").
db.employes.find({"departement_id": ObjectId("...")})  # Remplace "..." with the actual ObjectId of the department
# Trouver les employés ayant plus de 3 compétences.
db.employes.find({"competences": {"$size": {"$gt": 3}}})
# Trouver les employés dont le salaire est compris entre 500000 et 1000000.
db.employes.find({"contrat.salaire": {"$gte": 500000, "$lte": 1000000}})    
# Trouver les employés dont le nom contient "a" ou "e".
db.employes.find({"nom": {"$regex": "[ae]"}})
# Trouver les employés dont le nom ne contient pas "a".
db.employes.find({"nom": {"$not": {"$regex": "a"}})
# Trouver les employés dont le nom est "Edem Kodjo" ou "Julien Ayayi".
db.employes.find({"nom": {"$in": ["Edem Kodjo", "Julien Ayayi"]}})
#Afficher une liste simplifiée avec le nom et l’email uniquement.
db.employes.find({}, {"nom": 1, "email": 1, "_id": 0})
# Trouver les employés dont le nom commence par "A" et qui ont "MongoDB" dans leurs compétences.
db.employes.find({"nom": {"$regex": "^A"}, "competences": "MongoDB"})   
#Trouver tous les employés qui ont un champ competences.
db.employes.find({"competences": {"$exists": True}})
#Voir les employés qui occupent l’un de plusieurs postes.

ids_postes = [ObjectId("id1"), ObjectId("id2"), ObjectId("id3")]

db.employes.find({
    "poste_id": {"$in": ids_postes}
})
# Trouver les employés qui n'ont pas de compétences.
db.employes.find({"competences": {"$exists": False}})   
# Trouver les employés qui ont un contrat de type "CDD" ou "CDI".
db.employes.find({"contrat.type": {"$in": ["CDD", "CDI"]}})
