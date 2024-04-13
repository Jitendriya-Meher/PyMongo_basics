import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['PYMongo_CWH']
    collection = db['harry']

    old = {
        "name":"default",
    }
    newData = {
        "$set":{
            "marks":0
        }
    }

    updatedDatas = collection.update_many(old,newData)
    print("\nUpdated datas : " , updatedDatas)
    print("\nUpdated datas count : " , updatedDatas.modified_count)

    newData = {
        "$set":{
            "marks":100
        }
    }

    updatedData = collection.update_one(old,newData)
    print("\nUpdated data : " , updatedData)