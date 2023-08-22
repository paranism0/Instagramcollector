import motor.motor_asyncio
import pymongo
from ..models import env

class Database:
    def __init__(self):
        vars = env.Settings()
        self.client = motor.motor_asyncio.AsyncIOMotorClient(host = vars.MONGODB_HOST , port = vars.MONGODB_PORT)
        self.nonasyncclient = pymongo.MongoClient(host = vars.MONGODB_HOST , port = vars.MONGODB_PORT)
        self.nonasyncdb = self.nonasyncclient[vars.MONGODB_DATABASE]
        self.db = self.client.instaCollector
    async def insert(self , data , collection):
        return await collection.insert_one(data)
    async def select(self , filter , collection , many=False):
        if many:
            return await collection.find(filter)
        return await collection.find_one(filter)
    async def delete(self , filter ,collection , many = False):
        if many:
            return await collection.delete_one(filter)
        return await collection.delete_many(filter)