from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://sampathkumar4008:ea9IEuPRxnWyrcHE@debateai.mne98el.mongodb.net/?retryWrites=true&w=majority&appName=DEBATEAI"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)