from pymongo import MongoClient
from os import environ

uri = 'mongodb+srv://{username}:{password}@cluster-lhlongo-ir7ly.gcp.mongodb.net/test?retryWrites=true&w=majority'

db_user_name = environ['MONGO_USER']
db_user_password = environ['MONGO_PASSWORD']


client = MongoClient(uri.format(
    username=db_user_name, password=db_user_password))

collection = client.conversions_api.userConversions
