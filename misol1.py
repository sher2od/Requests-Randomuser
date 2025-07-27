import json
import requests

# 1. Foydalanuvchini API'dan olish
url = 'https://randomuser.me/api/'
response = requests.get(url)
data = response.json()  # JSON javobni Python dict'ga aylantiradi

# 2. Foydalanuvchi ma'lumotlarini ajratib olish
user = data['results'][0]

first_name = user['name']['first']
last_name = user['name']['last']
gender = user['gender']
email = user['email']
phone = user['phone']
street = user['location']['street']['name']
city = user['location']['city']
country = user['location']['country']

# 3. Ma'lumotni kerakli formatda tayyorlash
user_data = {
    "first_name": first_name,
    "last_name": last_name,
    "gender": gender,
    "email": email,
    "phone": phone,
    "address": {
        "street": street,
        "city": city,
        "country": country
    }
}

# 4. JSON faylga yozish — user1.json
with open('user1.json', 'w') as fayl:
    json.dump(user_data, fayl, indent=2)

print("✅ Ma'lumotlar user1.json faylga saqlandi.")
