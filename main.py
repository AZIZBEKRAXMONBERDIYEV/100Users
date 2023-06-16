import requests 
import json
from tinydb import TinyDB

url = 'https://randomuser.me/api/'

payload = {
    'results':100,
}
users = []
response = requests.get(url=url,params=payload)

if response.status_code == 200:
    users_data = response.json()['results']
    for user in users_data:
        users.append({
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
        
with open('users.json', 'w') as f:
    json.dump(users,f,indent=4)