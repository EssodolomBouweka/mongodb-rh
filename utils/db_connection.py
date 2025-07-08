from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

employees = db["employees"]
departments = db["departments"]
leave_requests = db["leave_requests"]

