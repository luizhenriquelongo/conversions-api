import json
import pymongo
from datetime import datetime
from os import getcwd
from dateutil.parser import parse
from config import collection

BASE_DIR = getcwd()

collection.create_index([("email", pymongo.TEXT)])

with open(f'{BASE_DIR}/src/static/teste-fullstack.json') as json_file:
    data = json.load(json_file)
    data = data['leads']
    for item in data:
        item['created'] = parse(item.get('created'))
    result = collection.insert_many(data)
