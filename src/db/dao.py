from pymongo import ReturnDocument
from datetime import datetime
from bson.json_util import dumps
from .config import collection
      

class MongoDao:

    def __init__(self, email):
        self.collection = collection
        self.__email = email

    @property
    def email(self):
        return self.__email

    def email_exists(self):
        result = collection.count_documents({"email": self.__email})
        if result:
            return True
        return False


    def insert_document(self, document, material):        
        result = collection.find_one_and_update(
            filter={'email': self.__email},
            update={'$set': document},
            upsert=True,
            return_document=ReturnDocument.AFTER,
        )

        if self.email_exists():
            update = {'$push': {"conversions": material}}
        else:
            update = {'$set': {"conversions": material}}

        result = collection.update_one(
            filter={'email': self.__email},
            update=update,
        )

        return result

    @staticmethod
    def get_contacts_created_count(initial_date: datetime, final_date: datetime):
        result = collection.count_documents({
            "created": {
                "$lte": final_date, "$gte": initial_date
            }
        })
        return result

    @staticmethod
    def get_contacts_with_no_empty_conversions_count(initial_date: datetime, final_date: datetime):
        results = collection.find({
            "created": {
                "$lte": final_date, "$gte": initial_date
            }
        })

        count = 0
        for result in results:
            if result.get('conversions'):
                count += 1

        return count

    @staticmethod
    def get_segmented_conversions_count(initial_date: datetime, final_date: datetime):
        results = collection.find({
            "created": {
                "$lte": final_date, "$gte": initial_date
            }
        })

        segmentation = {}

        for result in results:
            conversions_list = result.get('conversions')
            for item in conversions_list:
                material_name = item.get('material')
                if material_name not in segmentation:
                    segmentation[material_name] = 1
                else:
                    segmentation[material_name] += 1

        return segmentation
    
    @staticmethod
    def get_all():
        results = collection.find().limit(50)
        return dumps(results)            
