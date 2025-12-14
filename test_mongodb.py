from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_DB_URL"))

print("\nDatabases:")
print(client.list_database_names())

db = client["GaneshLakshmana"]
print("\nCollections in GaneshLakshmana:")
print(db.list_collection_names())

collection = db["Phishing_Data"]
print("\nDocument count:", collection.count_documents({}))
