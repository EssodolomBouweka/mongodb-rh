from utils.db_connection import employees, departments, leave_requests
from bson.objectid import ObjectId

class RHMongoDB:
    def __init__(self):
        self.employees = employees
        self.departments = departments
        self.leave_requests = leave_requests

    # ------------------------ CRUD ------------------------

    def insert_new_employee(self, employee: dict) -> str:
        """Ajoute un nouvel employé et retourne son ID MongoDB."""
        result = self.employees.insert_one(employee)
        return str(result.inserted_id)

    def find_all_employees(self) -> list:
        """Retourne la liste de tous les employés."""
        return list(self.employees.find())

    def update_employee_salary(self, email: str, new_salary: float) -> int:
        """
        Met à jour le salaire d'un employé identifié par son email.
        Retourne le nombre de documents modifiés.
        """
        result = self.employees.update_one({"email": email}, {"$set": {"salary": new_salary}})
        return result.modified_count

    def delete_employee(self, email: str) -> int:
        """
        Supprime un employé via son email.
        Retourne le nombre de documents supprimés.
        """
        result = self.employees.delete_one({"email": email})
        return result.deleted_count

    def find_employee_by_name(self, name: str) -> list:
        """Retourne la liste des employés dont le prénom correspond."""
        return list(self.employees.find({"first_name": name}))

    def find_departments(self) -> list:
        """Retourne la liste de tous les départements."""
        return list(self.departments.find())

    # ------------------- Requêtes avancées -------------------

    def find_employees_on_leave(self) -> list:
        """Retourne la liste des employés en congé."""
        return list(self.employees.find({"on_leave": True}))

    def find_employees_with_salary_range(self, min_sal: float, max_sal: float) -> list:
        """Retourne la liste des employés avec salaire compris entre min_sal et max_sal."""
        return list(self.employees.find({"salary": {"$gte": min_sal, "$lte": max_sal}}))

    def find_employees_matching_regex(self, pattern: str) -> list:
        """Retourne les employés dont le prénom correspond à une regex donnée."""
        return list(self.employees.find({"first_name": {"$regex": pattern}}))

    def find_employees_with_fields(self, fields: dict) -> list:
        """
        Retourne les employés avec uniquement les champs spécifiés.
        'fields' est un dict de projection MongoDB (ex : {"first_name": 1, "_id": 0}).
        """
        return list(self.employees.find({}, fields))

    def find_employees_with_or_condition(self, conditions: list) -> list:
        """
        Retourne les employés qui vérifient au moins une des conditions (liste de dict MongoDB).
        """
        return list(self.employees.find({"$or": conditions}))

    def find_employees_with_missing_field(self, field: str) -> list:
        """
        Retourne les employés ne possédant pas le champ 'field'.
        """
        return list(self.employees.find({field: {"$exists": False}}))

    # ------------------------ Agrégation ------------------------

    def get_average_salary_by_department(self) -> list:
        """Calcule la moyenne des salaires par département."""
        pipeline = [
            {"$group": {"_id": "$department_id", "avg_salary": {"$avg": "$salary"}}}
        ]
        return list(self.employees.aggregate(pipeline))

    def get_top_paid_employees(self, limit=3) -> list:
        """Retourne les 'limit' employés les mieux payés."""
        return list(self.employees.find().sort("salary", -1).limit(limit))

    def count_employees_by_department(self) -> list:
        """Compte le nombre d'employés par département."""
        pipeline = [
            {"$group": {"_id": "$department_id", "count": {"$sum": 1}}}
        ]
        return list(self.employees.aggregate(pipeline))

    def join_employee_department(self) -> list:
        """
        Effectue une jointure entre employés et départements,
        enrichissant chaque employé avec les infos de son département.
        """
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
        return list(self.employees.aggregate(pipeline))

    def get_leave_count_by_employee(self) -> list:
        """Compte le nombre total de congés pris par chaque employé."""
        pipeline = [
            {"$group": {"_id": "$employee_email", "total_leaves": {"$sum": 1}}}
        ]
        return list(self.leave_requests.aggregate(pipeline))

    def get_approved_leaves(self) -> list:
        """Retourne tous les congés approuvés."""
        pipeline = [{"$match": {"status": "approuvé"}}]
        return list(self.leave_requests.aggregate(pipeline))

    def get_longest_leave(self) -> dict:
        """
        Trouve le congé le plus long en calculant la durée entre 'start_date' et 'end_date'.
        Retourne un document (dict) ou None si aucun congé.
        """
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
        results = list(self.leave_requests.aggregate(pipeline))
        return results[0] if results else None

    def group_employees_by_position(self) -> list:
        """Regroupe les employés par poste et compte leur nombre."""
        pipeline = [
            {"$group": {"_id": "$position", "count": {"$sum": 1}}}
        ]
        return list(self.employees.aggregate(pipeline))





rh = RHMongoDB()

# Ajouter un employé
emp = {
    "first_name": "Alice",
    "last_name": "Dupont",
    "email": "alice.dupont@example.com",
    "salary": 3500,
    "department_id": ObjectId("..."),
    "position": "Développeur",
    "on_leave": False
}
emp_id = rh.insert_new_employee(emp)
print(f"Employé créé avec ID : {emp_id}")

# Afficher tous les employés
all_emps = rh.find_all_employees()
for e in all_emps:
    print(e)

# Mettre à jour salaire
updated = rh.update_employee_salary("alice.dupont@example.com", 4000)
print(f"{updated} document(s) modifié(s)")

