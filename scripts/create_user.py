from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def create_mongo_user(username: str, password: str, db_name: str, roles: list):
    """
    Crée un utilisateur MongoDB avec les rôles spécifiés.

    Args:
        username (str): Nom de l'utilisateur à créer.
        password (str): Mot de passe de l'utilisateur.
        db_name (str): Nom de la base de données où l'utilisateur aura ses rôles.
        roles (list): Liste des rôles (ex: [{"role": "readWrite", "db": db_name}]).

    Returns:
        None
    """
    try:
        client = MongoClient(os.getenv("MONGO_LOCAL_URI"))
        db = client[db_name]
        db.command("createUser", username, pwd=password, roles=roles)
        print(f"Utilisateur '{username}' créé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la création de l'utilisateur '{username}': {e}")


if __name__ == "__main__":
    USERNAME = "stagiaire"
    PASSWORD = "stagiaire123"
    DB_NAME = os.getenv("DB_NAME")
    ROLES = [{"role": "readWrite", "db": DB_NAME}]

    create_mongo_user(USERNAME, PASSWORD, DB_NAME, ROLES)
