import requests 
import json
from tinydb import TinyDB

url = 'https://randomuser.me/api/'

payload = {
    'results':100,
}

response = requests.get(url=url,params=payload)

db = TinyDB('users.json', indent=4)
users = db.table('users')


if response.status_code == 200:
    users_data = response.json()['results']
    for user in users_data:
        users.insert({
            'first_name':user['name']['first'],
            'last_name':user['name']['last'],
            'age':user['dob']['age'],
            'gender':user['gender'],
            'email':user['email'],
            'city':user['location']['city'],
            'country':user['location']['country'],
            'phone':user['phone'],
            'nat':user['nat']
        })
        
