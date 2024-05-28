import re
from pymongo import MongoClient

database_name = 'project_db'
mongodb_port = 27017
uri = f'mongodb://localhost:{mongodb_port}/'
mongo_db_client = MongoClient(uri)
db = mongo_db_client[database_name]

collection_user = db['user_details']
collection_token = db['token_details']

def register_user(request_data):

    collection_user.insert_one({'emailid': request_data['emailid'], 'password': request_data['password'],
                    'name':request_data['name'],"company":request_data['company']})
    return 'Success'

def login_user(request_data):
    resp = collection_user.find_one({'emailid': request_data['emailid'], 'password': request_data['password']})
    print(resp)
    if not resp:
        return 'User not registered
    return "Success"