from pymongo import MongoClient
from decouple import config



def get_unidata_qa():
    url = config('MONGO_URL')

    client = MongoClient(url)

    db = client['UniDataQA']

    return db



