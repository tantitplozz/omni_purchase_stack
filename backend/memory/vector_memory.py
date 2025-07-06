import pymongo
import os

def log_result(task, result):
    client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
    db = client[os.getenv("MONGODB_DB_NAME")]
    db["purchase_logs"].insert_one({"task": task, "result": result})
