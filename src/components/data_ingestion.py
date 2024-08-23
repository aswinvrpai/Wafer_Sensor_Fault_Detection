import csv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://aswin199vr:oSZS4Lu1MTPh1CJi@phishingclassifier.4emhaa4.mongodb.net/?retryWrites=true&w=majority&appName=PhishingClassifier"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db=client["CSV"]
csv_file=r"C:\Work_Directory\Learn\DS_Projects\Prediction_Diamond_Price\notebooks\data\gemstone.csv"
collection=db['csv_diamond']

with open(csv_file,'r') as fopen:
    reader=csv.DictReader(fopen)
    
    for row in reader:
        collection.insert_one(row)
        
if(collection.count_documents({}) != 0):
    print('csv data imported')