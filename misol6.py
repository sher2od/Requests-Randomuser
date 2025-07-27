import csv
import requests

# API'dan ma'lumot olish
url = 'https://randomuser.me/api/?results=10'
response = requests.get(url)
data = response.json()

# CSV faylga yozish
with open('users.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Full Name', 'Gender', 'Email', 'Phone', 'Country'])  # Sarlavhalar

    for user in data['results']:
        full_name = f"{user['name']['first']} {user['name']['last']}"
        gender = user['gender']
        email = user['email']
        phone = user['phone']
        country = user['location']['country']

        writer.writerow([full_name, gender, email, phone, country])

print("✅ users.csv faylga yozildi.")
