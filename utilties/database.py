import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
database = os.getenv('MONGODB') 

client = pymongo.MongoClient(database)# server.local_bind_port is assigned local port
db = client['nya']
users = db['users']

async def getUserData(id):
    profile = users.find_one({"discordid": id})
    if profile is None:
        users.insert_one({"discordid": id, "wynncraftName": None})
        print("new user created")
    profile = users.find_one({"discordid": id}) 
    return profile

async def updateUserData(query, newItem):
    newvalues = { "$set": newItem }
    return await users.update_one(query, newvalues)