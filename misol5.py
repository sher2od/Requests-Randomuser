import json
import requests
from datetime import datetime

# 20 ta foydalanuvchini olish
url = 'https://randomuser.me/api/?results=20'
response = requests.get(url)
data = response.json()

young_users = []

for user in data['results']:
    # Tug‘ilgan yilni olish
    dob = user['dob']['date']
    birth_year = int(dob[:4])

    if birth_year > 1990:
        full_name = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        young_users.append({
            'name': full_name,
            'birth_year': birth_year,
            'email': email
        })

# JSON faylga yozish
with open('young_users.json', 'w', encoding='utf-8') as f:
    json.dump(young_users, f, indent=2)

print("young_users.json faylga yozildi.")
