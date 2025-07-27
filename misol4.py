import json 
import requests

url = 'https://randomuser.me/api/?results=1'
responce = requests.get(url)

data = responce.json()

users_list = []

for user in data['results']:
    full_name = f"{user['name']['first']} {user['name']['last']}"
    email = f"{user['email']}"
    picture = f"{user['picture']['large']}"

    users_list.append({
        "name":full_name,
        "email":email,
        "image_url":picture
    })

with open('users_with_images.json','w') as jfile:
    json.dump(users_list,jfile,indent=2)

print("Yozildi")