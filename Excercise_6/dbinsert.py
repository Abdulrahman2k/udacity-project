import json
import pprint

def insert_data(data, db):
    db.dubai.insert( data )

    # Your code here. Insert the data into a collection 'arachnid'

    pass


if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    with open('dubai_abu-dhabi.osm.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        #pprint.pprint db.dubai.find_one()