import pymongo
import os
from dotenv import load_dotenv
load_dotenv()
database = os.getenv('DATABASE') 
mongodb = pymongo.MongoClient(database)["nya"]
users = mongodb["users"]

def getUserData(id):
    profile = users.find_one({"discordid": id})
    if profile is None:
        users.insert_one({"discordid": id, "wynncraftName": None})
        print("new user created")
    profile = users.find_one({"discordid": id}) 
    return profile

def updateUserData(query, newItem):
    newvalues = { "$set": newItem }
    users.update_one(query, newvalues)