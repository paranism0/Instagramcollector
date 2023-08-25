from fastapi import HTTPException , status
from .client import Client
import restapi
from hashlib import md5

class handleInstagram(restapi.handleInstaAccounts.Accounts):
    def __init__(self):
        super().__init__()

    @staticmethod
    def raise_error(msg = "Bad Request , Invalid username and password"):
        raise HTTPException(
              status_code=status.HTTP_400_BAD_REQUEST,
              detail=msg,
            )

    @staticmethod
    def generate_id(user,pwd):
        return md5((user + pwd).encode()).hexdigest()

    async def login(self , username , password):
        try:
            client = Client(username=username , password=password)
            username = client.username
            if username:
               cookie = client.cookie_jar
               _id = handleInstagram.generate_id(username , password)
               await self.update({"_id":_id},{"$set":{"username" : username , "cookie" : cookie}} , self.accounts)
               return {"success" : True , "cookie" : cookie , "accountId" : _id}
            handleInstagram.raise_error()
        except:
           handleInstagram.raise_error()
    
    async def get_followers(self , account_id , username):
        try:
            cookie = (await self.select({"_id":account_id},self.accounts)).get("cookie")
            client = Client(username="" , password="" , cookie = cookie)
            followers = client.user_followers(client.username_info(username)["user"]["pk"] , client.generate_uuid())
            return {"success":True , "followers_list" : [p["username"] for p in followers["users"]]}
        except Exception as e:
            handleInstagram.raise_error("Bad Request")