
# 📚 Projet MongoDB RH – Rapport Final

**Étudiant :** Essodolom BOUWEKA  
**Module :** Bases de Données NoSQL avec MongoDB  
**Technologie :** PyMongo (Python)  
**Sujet :** Système de gestion RH avec MongoDB

---

## 🎯 Objectif du projet

Concevoir un système d'information complet pour la gestion des ressources humaines avec MongoDB.  
L’objectif est de modéliser, insérer et interroger les données d’un domaine métier RH via PyMongo.

---

## 🧱 Modélisation (3 collections)

- **employes** : informations sur le personnel
- **postes** : postes occupés avec grilles salariales
- **departements** : services et chefs de département

### 📁 Exemple `employes`
```json
{
  "nom": "Essodolom Bouweka",
  "email": "essodolom.bouweka@entreprise.tg",
  "date_embauche": "2022-03-15",
  "poste_id": ObjectId("..."),
  "departement_id": ObjectId("..."),
  "competences": ["Python", "MongoDB", "Power BI"],
  "contrat": {
    "type": "CDI",
    "salaire": 800000,
    "date_debut": "2022-03-15"
  }
}
```

---

## 🗃️ Données
- Générées automatiquement via `Faker`
- 20 documents par collection (employes, postes, departements)
- Import via `insert_data.py`

---

## 🔄 Requêtes CRUD (6)
```python
# Ajouter un employé
db.employes.insert_one({...})

# Lire tous les employés
db.employes.find()

# Mise à jour de salaire
db.employes.update_one({"email": "..."}, {"$set": {"contrat.salaire": 900000}})

# Supprimer un employé
db.employes.delete_one({"email": "..."})
```

---

## 🔍 Requêtes avancées (6)
```python
# Regex sur nom
db.employes.find({"nom": {"$regex": "^A", "$options": "i"}})

# Projection spécifique
db.employes.find({}, {"nom": 1, "email": 1, "_id": 0})

# Requête avec $or
db.employes.find({
    "$or": [{"contrat.type": "CDI"}, {"contrat.salaire": {"$gt": 800000}}]
})
```

---

## 📊 Agrégations (8)
```python
# Moyenne des salaires par contrat
db.employes.aggregate([
    {"$group": {"_id": "$contrat.type", "salaire_moyen": {"$avg": "$contrat.salaire"}}}
])

# Jointure avec postes
db.employes.aggregate([
    {"$lookup": {"from": "postes", "localField": "poste_id", "foreignField": "_id", "as": "poste"}},
    {"$unwind": "$poste"}
])

# Nombre d'employés par compétence
db.employes.aggregate([
    {"$unwind": "$competences"},
    {"$group": {"_id": "$competences", "nb": {"$sum": 1}}}
])
```

---

## ✨ Fonctionnalités bonus (main.py)
- Lister les employés par département
- Afficher toutes les compétences distinctes
- Compter les contrats par type (CDI, CDD, Stage)
- Exporter les employés en CSV

---

## 📁 Structure du projet
```
Projet_MongoDB_RH/
├── data/                  # Données JSON
├── scripts/               # Insertion, utilisateur Mongo
├── queries/               # Requêtes CRUD, avancées, agrégation
├── main.py                # Menu interactif en CLI
├── README.md              # Documentation projet
├── .env                   # Connexion MongoDB
└── requirements.txt
```

---

##  Résultat final

- 3 collections liées avec des données réalistes
- 20 requêtes documentées
- Fonctions d'analyse RH enrichies
- Projet prêt à être déployé localement ou sur MongoDB Atlas

---




departement
//  Embedding ✅
//Pourquoi ?
// Le champ chef_dept contient un sous-document (nom, email) directement imbriqué dans le document departement.

//on n’a pas utilises pas d’identifiant (ObjectId) de référence pointant vers une autre collection, ce qui serait le cas avec le referencing.

// En résumé :
// Approche	Type	Justification
// Embedding	✅ Utilisé ici	On intègre directement les infos du chef dans le document departement.

// Pourquoi ce choix est pertinent ici ?
// Les données du chef de département sont faiblement réutilisables ailleurs.

// Elles sont intrinsèquement liées au département (le chef est propre à un seul département).

// Pas besoin de faire des jointures coûteuses avec $lookup.



postes
// Referencing 
// Pourquoi ?
// Les champs poste_id et departement_id contiennent des identifiants UUID (ou ObjectId) pointant vers d'autres collections : postes, departements

//Ces identifiants ne sont pas des sous-documents, donc les données du poste ou du département ne sont pas directement incluses dans le document employé.

// Raisons pour lesquelles le referencing est pertinent ici :

// Réutilisabilité	Plusieurs employés peuvent partager le même poste ou département.
// Évite la duplication	Pas besoin de répéter les mêmes infos de poste ou de service dans chaque employé.
// Requêtes combinées	Tu peux facilement faire un $lookup pour récupérer les données liées.


