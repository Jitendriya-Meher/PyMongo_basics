import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017")

    allDBs = client.list_database_names()
    print("\nAll databases: " , allDBs)

    collection = client['PYMongo_CWH']
    print("\nCollection list: " , collection.list_collection_names())
