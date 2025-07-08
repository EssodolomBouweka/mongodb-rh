from rh_mongodb import RHMongoDB
from bson.objectid import ObjectId
import re
from datetime import datetime

# Fonction pour paginer une liste d'items (affichage par pages)
def paginate(items, page_size=5):
    total = len(items)
    for start in range(0, total, page_size):
        yield items[start:start+page_size]

# Fonction pour saisir un ObjectId MongoDB avec validation
def input_object_id(prompt):
    val = input(prompt).strip()
    if val == "":
        return None
    try:
        return ObjectId(val)
    except:
        print("⚠️ ID invalide, champ ignoré.")
        return None

# Fonction pour saisir un email avec validation par regex
def input_email(prompt):
    while True:
        email = input(prompt).strip()
        if email == "":
            return None
        # Validation simple d'email avec expression régulière
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        print("❌ Email invalide, réessayez.")

# Fonction pour saisir une valeur numérique (float) avec gestion d'erreur
def input_float(prompt, allow_empty=False):
    while True:
        val = input(prompt).strip()
        if allow_empty and val == "":
            return None
        try:
            return float(val)
        except ValueError:
            print("❌ Valeur numérique invalide, réessayez.")

# Fonction pour saisir une date au format YYYY-MM-DD avec validation
def input_date(prompt, allow_empty=False):
    while True:
        val = input(prompt).strip()
        if allow_empty and val == "":
            return None
        try:
            datetime.strptime(val, "%Y-%m-%d")
            return val
        except ValueError:
            print("❌ Format date invalide (YYYY-MM-DD), réessayez.")

# Fonction demandant une confirmation Oui/Non
def confirmer_action(message):
    choix = input(f"{message} (o/n) : ").lower()
    return choix == 'o'

# Affiche les employés avec pagination et confirmation avant page suivante
def afficher_employes(rh):
    employes = list(rh.find_all_employees())
    if not employes:
        print("Aucun employé trouvé.")
        return
    for page_num, page in enumerate(paginate(employes), 1):
        print(f"\n--- Page {page_num} ---")
        for e in page:
            print(f"{e.get('first_name', '')} {e.get('last_name', '')} - {e.get('email')} - Salaire: {e.get('salary', 'N/A')}")
        if page_num * 5 >= len(employes):
            print("--- Fin de la liste ---")
            break
        if not confirmer_action("Voir la page suivante ?"):
            break

# Affiche les départements avec pagination
def afficher_departements(rh):
    departements = list(rh.departments.find())
    if not departements:
        print("Aucun département trouvé.")
        return
    for page_num, page in enumerate(paginate(departements), 1):
        print(f"\n--- Page {page_num} ---")
        for d in page:
            print(f"ID: {d['_id']} | Nom: {d.get('nom', '')} | Budget: {d.get('budget', 'N/A')}")
        if page_num * 5 >= len(departements):
            print("--- Fin de la liste ---")
            break
        if not confirmer_action("Voir la page suivante ?"):
            break

# Affiche les postes avec pagination
def afficher_postes(rh):
    postes = list(rh.positions.find())
    if not postes:
        print("Aucun poste trouvé.")
        return
    for page_num, page in enumerate(paginate(postes), 1):
        print(f"\n--- Page {page_num} ---")
        for p in page:
            print(f"ID: {p['_id']} | Titre: {p.get('titre', '')} | Niveau: {p.get('niveau_experience', 'N/A')}")
        if page_num * 5 >= len(postes):
            print("--- Fin de la liste ---")
            break
        if not confirmer_action("Voir la page suivante ?"):
            break

def main():
    rh = RHMongoDB()  # Initialisation de la connexion MongoDB via classe dédiée

    # Menus textuels pour navigation dans l'application
    def menu_principal():
        print("\n=== MENU RH MongoDB ===")
        print("1. Gérer les employés")
        print("2. Gérer les départements")
        print("3. Gérer les postes")
        print("0. Quitter")

    def menu_employes():
        print("\n--- Employés ---")
        print("1. Afficher tous les employés")
        print("2. Ajouter un employé")
        print("3. Mettre à jour salaire")
        print("4. Supprimer un employé")
        print("5. Rechercher par prénom")
        print("0. Retour")

    def menu_departements():
        print("\n--- Départements ---")
        print("1. Afficher tous les départements")
        print("2. Ajouter un département")
        print("3. Mettre à jour un budget")
        print("4. Supprimer un département")
        print("0. Retour")

    def menu_postes():
        print("\n--- Postes ---")
        print("1. Afficher tous les postes")
        print("2. Ajouter un poste")
        print("3. Mettre à jour la description")
        print("4. Supprimer un poste")
        print("0. Retour")

    # Boucle principale du programme
    while True:
        menu_principal()
        choix = input("Choix principal : ").strip()

        if choix == "1":
            # Gestion des employés
            while True:
                menu_employes()
                c = input("Choix employés : ").strip()
                if c == "1":
                    afficher_employes(rh)
                elif c == "2":
                    print("\n--- Ajouter un employé ---")
                    first_name = input("Prénom : ").strip()
                    last_name = input("Nom : ").strip()
                    email = input_email("Email : ")
                    salary = input_float("Salaire : ")
                    dept_id = input_object_id("ID département (laisser vide si inconnu) : ")
                    position = input("Poste : ").strip()
                    on_leave = input("En congé ? (oui/non) : ").strip().lower() == "oui"

                    # Création dictionnaire employé
                    emp = {
                        "first_name": first_name,
                        "last_name": last_name,
                        "email": email,
                        "salary": salary,
                        "department_id": dept_id,
                        "position": position,
                        "on_leave": on_leave
                    }
                    emp_id = rh.insert_new_employee(emp)  # Insertion en base
                    print(f"✅ Employé ajouté avec ID : {emp_id}")

                elif c == "3":
                    # Mise à jour du salaire d'un employé existant
                    email = input_email("Email de l'employé : ")
                    new_salary = input_float("Nouveau salaire : ")
                    if confirmer_action(f"Confirmer la mise à jour du salaire de {email} à {new_salary} ?"):
                        modif = rh.update_employee_salary(email, new_salary)
                        print("✅ Salaire mis à jour." if modif else "❌ Employé non trouvé.")
                    else:
                        print("Modification annulée.")

                elif c == "4":
                    # Suppression d'un employé
                    email = input_email("Email de l'employé à supprimer : ")
                    if confirmer_action(f"Confirmer la suppression de l'employé {email} ?"):
                        supp = rh.delete_employee(email)
                        print("✅ Employé supprimé." if supp else "❌ Employé non trouvé.")
                    else:
                        print("Suppression annulée.")

                elif c == "5":
                    # Recherche par prénom
                    name = input("Prénom à rechercher : ").strip()
                    results = rh.find_employee_by_name(name)
                    if results:
                        for emp in results:
                            print(f"{emp.get('first_name')} {emp.get('last_name')} - {emp.get('email')}")
                    else:
                        print("Aucun employé trouvé.")

                elif c == "0":
                    break
                else:
                    print("⛔ Choix invalide.")

        elif choix == "2":
            # Gestion des départements
            while True:
                menu_departements()
                c = input("Choix départements : ").strip()
                if c == "1":
                    afficher_departements(rh)

                elif c == "2":
                    # Ajout d'un département
                    print("\n--- Ajouter un département ---")
                    nom = input("Nom : ").strip()
                    description = input("Description : ").strip()
                    budget = input_float("Budget : ")
                    date_creation = input_date("Date de création (YYYY-MM-DD) : ")

                    dept = {
                        "nom": nom,
                        "description": description,
                        "budget": budget,
                        "date_creation": date_creation
                    }
                    result = rh.departments.insert_one(dept)
                    print(f"✅ Département ajouté avec ID : {result.inserted_id}")

                elif c == "3":
                    # Mise à jour du budget
                    nom = input("Nom du département à modifier : ").strip()
                    nouveau_budget = input_float("Nouveau budget : ")
                    if confirmer_action(f"Confirmer la mise à jour du budget du département {nom} à {nouveau_budget} ?"):
                        res = rh.departments.update_one({"nom": nom}, {"$set": {"budget": nouveau_budget}})
                        print("✅ Budget mis à jour." if res.modified_count > 0 else "❌ Département non trouvé ou pas modifié.")
                    else:
                        print("Modification annulée.")

                elif c == "4":
                    # Suppression d'un département
                    nom = input("Nom du département à supprimer : ").strip()
                    if confirmer_action(f"Confirmer la suppression du département {nom} ?"):
                        res = rh.departments.delete_one({"nom": nom})
                        print("✅ Département supprimé." if res.deleted_count > 0 else "❌ Département non trouvé.")
                    else:
                        print("Suppression annulée.")

                elif c == "0":
                    break
                else:
                    print("⛔ Choix invalide.")

        elif choix == "3":
            # Gestion des postes
            while True:
                menu_postes()
                c = input("Choix postes : ").strip()
                if c == "1":
                    afficher_postes(rh)

                elif c == "2":
                    # Ajout d'un poste
                    print("\n--- Ajouter un poste ---")
                    titre = input("Titre : ").strip()
                    description = input("Description : ").strip()
                    niveau_exp = input("Niveau d'expérience : ").strip()
                    date_creation = input_date("Date de création (YYYY-MM-DD) : ")

                    poste = {
                        "titre": titre,
                        "description": description,
                        "niveau_experience": niveau_exp,
                        "date_creation": date_creation
                    }
                    result = rh.positions.insert_one(poste)
                    print(f"✅ Poste ajouté avec ID : {result.inserted_id}")

                elif c == "3":
                    # Mise à jour de la description d'un poste
                    titre = input("Titre du poste à modifier : ").strip()
                    nouvelle_desc = input("Nouvelle description : ").strip()
                    if confirmer_action(f"Confirmer la mise à jour de la description du poste {titre} ?"):
                        res = rh.positions.update_one({"titre": titre}, {"$set": {"description": nouvelle_desc}})
                        print("✅ Description mise à jour." if res.modified_count > 0 else "❌ Poste non trouvé ou pas modifié.")
                    else:
                        print("Modification annulée.")

                elif c == "4":
                    # Suppression d'un poste
                    titre = input("Titre du poste à supprimer : ").strip()
                    if confirmer_action(f"Confirmer la suppression du poste {titre} ?"):
                        res = rh.positions.delete_one({"titre": titre})
                        print("✅ Poste supprimé." if res.deleted_count > 0 else "❌ Poste non trouvé.")
                    else:
                        print("Suppression annulée.")

                elif c == "0":
                    break
                else:
                    print("⛔ Choix invalide.")

        elif choix == "0":
            print("Au revoir 👋")
            break

        else:
            print("⛔ Choix invalide.")

if __name__ == "__main__":
    main()
