import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['PYMongo_CWH']
    collection = db['harry']

    data = collection.find_one({
        "name":"amit"
    })
    print("\ndata: " , data)

    allDatas = collection.find({
        "name":"amit"
    }).limit(5)
    print("\nall Datas: " , allDatas)

    for item in allDatas:
        print("item: " , item)


    # logic to get all docs and hide some columns 
    allDocs = collection.find({},{
        "name":1,
        "_id":0
    })
    print("\nallDocs: " , allDocs)

    for item in allDocs:
        print("item: " , item)
    