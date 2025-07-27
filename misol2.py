import json
import requests

# 1. API'dan 10 ta foydalanuvchini olish
url = 'https://randomuser.me/api/?results=10'
response = requests.get(url)
data = response.json()  # JSON javobni dict'ga aylantiradi

# 2. Foydalanuvchilar ro'yxatini olish
users_list = []

for user in data['results']:
    full_name = f"{user['name']['first']} {user['name']['last']}"
    email = user['email']
    gender = user['gender']
    country = user['location']['country']

    users_list.append({
        "full_name": full_name,
        "email": email,
        "gender": gender,
        "country": country
    })

# 3. Natijani users.json faylga yozish
with open('users.json','w',encoding='utf-8') as fayl:
    json.dump(users_list, fayl, indent=2)

print("✅ 10 ta foydalanuvchi users.json faylga saqlandi.")
