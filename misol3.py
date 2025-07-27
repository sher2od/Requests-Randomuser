import json
import requests

url = 'https://randomuser.me/api/?results=10&gender=female'
responce = requests.get(url)
data = responce.json()

users_list = []

for user in data['results']:
    full_name = f"{user['name']['first']} {user['name']['last']}"
    email = user['email']
    phone = user['phone']
    country = user['location']['country']

    users_list.append({
        "full_name":full_name,
        "email":email,
        "Phone":phone,
        "country":country
    })

with open('user3.json','w',encoding='utf-8') as f:
    json.dump(users_list,f,indent=2)

print("Tayyor")
