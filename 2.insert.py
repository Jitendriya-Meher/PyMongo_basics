import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017")
    print("\nclient: " , client)

    db = client['PYMongo_CWH']
    print("\ndb: " , db)

    collection = db['harry']
    print("\ncollection: " , collection)

    # dict = {
    #     "name":"harry",
    #     'marks':50
    # }
    # dbData = collection.insert_one(dict)
    # print("\ndb data: " , dbData)

    # dicts = [
    #     {
    #         "name":"harry2",
    #         "marks":90
    #     },
    #     {
    #         "name":"harry3",
    #         "marks":10
    #     }
    # ]
    # dbDatas = collection.insert_many(dicts)
    # print("\ndb datas: " , dbDatas)

    print("\nEnter the Data to be inserted into the database")
    name = input("Enter Your Name : ")
    marks = int(input("Enter Your Marks : "))

    dict = {
        "name":name,
        "marks":marks
    }
    dbData = collection.insert_one(dict)
    print("\ndb data: " , dbData)