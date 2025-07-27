import requests
import os

# API'dan 5 ta foydalanuvchi olish
url = 'https://randomuser.me/api/?results=5'
response = requests.get(url)
data = response.json()

# Rasm saqlanadigan papkani yaratish (agar mavjud bo'lmasa)
os.makedirs('images', exist_ok=True)

# Har bir foydalanuvchining rasmini yuklab olish
for i, user in enumerate(data['results'], start=1):
    image_url = user['picture']['large']
    image_data = requests.get(image_url).content

    with open(f'images/user{i}.jpg', 'wb') as f:
        f.write(image_data)

print("✅ Barcha rasm fayllari 'images/' papkaga saqlandi.")
