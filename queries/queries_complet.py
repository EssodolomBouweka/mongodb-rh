from utils.db_connection import employees, departments, leave_requests

# ------------------------ CRUD ------------------------

def insert_new_employee(employee):
    """Ajouter un nouvel employé."""
    result = employees.insert_one(employee)
    print("✅ Employé ajouté avec ID :", result.inserted_id)

def find_all_employees():
    """Afficher tous les employés."""
    for emp in employees.find():
        print(emp)

def update_employee_salary(email, new_salary):
    """Mettre à jour le salaire d’un employé."""
    employees.update_one({"email": email}, {"$set": {"salary": new_salary}})
    print(f"✅ Salaire mis à jour pour {email}")

def delete_employee(email):
    """Supprimer un employé via son email."""
    employees.delete_one({"email": email})
    print(f"🗑️ Employé supprimé : {email}")

def find_employee_by_name(name):
    """Trouver des employés par nom."""
    for emp in employees.find({"first_name": name}):
        print(emp)

def find_departments():
    """Afficher tous les départements."""
    for dept in departments.find():
        print(dept)

# ------------------- Requêtes avancées -------------------

def find_employees_on_leave():
    """Trouver les employés en congé."""
    for emp in employees.find({"on_leave": True}):
        print(emp)

def find_employees_with_salary_range(min_sal, max_sal):
    """Trouver les employés dans une fourchette de salaire."""
    for emp in employees.find({"salary": {"$gte": min_sal, "$lte": max_sal}}):
        print(emp)

def find_employees_matching_regex():
    """Employés dont le nom commence par A (regex)."""
    for emp in employees.find({"first_name": {"$regex": "^A"}}):
        print(emp)

def find_employees_with_fields():
    """Afficher nom, prénom et poste uniquement."""
    for emp in employees.find({}, {"_id": 0, "first_name": 1, "last_name": 1, "position": 1}):
        print(emp)

def find_employees_with_or_condition():
    """Employés en congé ou gagnant plus de 2000."""
    for emp in employees.find({"$or": [{"on_leave": True}, {"salary": {"$gt": 2000}}]}):
        print(emp)

def find_employees_with_missing_field():
    """Employés sans département défini."""
    for emp in employees.find({"department_id": {"$exists": False}}):
        print(emp)

# ------------------------ Agrégation ------------------------

def get_average_salary_by_department():
    """Moyenne des salaires par département."""
    pipeline = [
        {"$group": {"_id": "$department_id", "avg_salary": {"$avg": "$salary"}}}
    ]
    for doc in employees.aggregate(pipeline):
        print(doc)

def get_top_paid_employees():
    """Top 3 des employés les mieux payés."""
    for emp in employees.find().sort("salary", -1).limit(3):
        print(emp)

def count_employees_by_department():
    """Nombre d'employés par département."""
    pipeline = [
        {"$group": {"_id": "$department_id", "count": {"$sum": 1}}}
    ]
    for doc in employees.aggregate(pipeline):
        print(doc)

def join_employee_department():
    """Jointure entre employés et départements."""
    pipeline = [
        {
            "$lookup": {
                "from": "departments",
                "localField": "department_id",
                "foreignField": "_id",
                "as": "department_info"
            }
        },
        {"$unwind": "$department_info"}
    ]
    for doc in employees.aggregate(pipeline):
        print(doc)

def get_leave_count_by_employee():
    """Nombre de congés pris par employé."""
    pipeline = [
        {"$group": {"_id": "$employee_email", "total_leaves": {"$sum": 1}}}
    ]
    for doc in leave_requests.aggregate(pipeline):
        print(doc)

def get_approved_leaves():
    """Lister tous les congés approuvés."""
    pipeline = [
        {"$match": {"status": "approuvé"}}
    ]
    for doc in leave_requests.aggregate(pipeline):
        print(doc)

def get_longest_leave():
    """Le congé le plus long."""
    pipeline = [
        {
            "$project": {
                "employee_email": 1,
                "duration": {
                    "$subtract": [{"$toDate": "$end_date"}, {"$toDate": "$start_date"}]
                }
            }
        },
        {"$sort": {"duration": -1}},
        {"$limit": 1}
    ]
    for doc in leave_requests.aggregate(pipeline):
        print(doc)

def group_employees_by_position():
    """Regrouper les employés par poste."""
    pipeline = [
        {"$group": {"_id": "$position", "count": {"$sum": 1}}}
    ]
    for doc in employees.aggregate(pipeline):
        print(doc)
