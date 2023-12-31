import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
database = os.getenv('MONGODB') 

client = pymongo.MongoClient(database)# server.local_bind_port is assigned local port
db = client['nya']
users = db['users']

async def initUserData(id):
    profile = users.find_one({"discordid": id})
    if profile is None:
        users.insert_one({"discordid": id, "wynncraft": None})

async def getUserData(id):
    await initUserData(id)
    profile = users.find_one({"discordid": id}) 
    return profile

async def updateUserData(query, newItem):
    newvalues = { "$set": newItem }
    users.update_one(query, newvalues)