'''
"How was working with MongoDB different from working with
PostgreSQL? What was easier, and what was harder?"


'''


import pymongo
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.test_database
print("----------------")
print("DB:", type(db), db)

print("----------------")
print("Collections:")
print(db.list_collection_names())