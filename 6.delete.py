import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['PYMongo_CWH']
    collection = db['harry']

    old = {
        "name":"del",
    }
    
    deletedData = collection.delete_one(old)
    print("\ndelete data: " , deletedData)

    deletedDatas = collection.delete_many(old)
    print("\ndelete datas: " , deletedDatas)
    print("\ndelete datas count: " , deletedDatas.deleted_count)

   