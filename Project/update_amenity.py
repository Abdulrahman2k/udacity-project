from pymongo import MongoClient
import pprint

Client = MongoClient("mongodb://localhost:27017")
db = Client.local

def main():
    amenity = db.dubai.find_one({"amenity":"Jebel Ali Station"})
    amenity["amenity"]="bureau_de_change"
    db.dubai.save(amenity)
if __name__ =="__main__":
    main()