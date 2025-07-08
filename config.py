import os
from dotenv import load_dotenv

load_dotenv()

MONGO_MODE = os.getenv("MONGO_MODE", "local")  # 'local' ou 'atlas'

if MONGO_MODE == "atlas":
    MONGO_URI = os.getenv("MONGO_ATLAS_URI")
else:
    MONGO_URI = os.getenv("MONGO_LOCAL_URI")

DB_NAME = "rh_management"
