
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

## ✅ Résultat final

- 3 collections liées avec des données réalistes
- 20 requêtes documentées
- Fonctions d'analyse RH enrichies
- Projet prêt à être déployé localement ou sur MongoDB Atlas

---

## 📅 Remise

- **Date limite :** 09 juillet 2025 à 23h59  
- **À envoyer par mail :** avosse28@gmail.com (fichier PDF)  
- **Code source :** GitHub ou GitLab (accès via lien ou invitation)
