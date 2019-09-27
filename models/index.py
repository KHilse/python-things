from pymongo import MongoClient
import os
mongo_client = os.environ.get('MONGODB_URI', default='mongodb://localhost:27017')
db = client['python-things']

