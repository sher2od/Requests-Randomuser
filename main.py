import json
import requests

url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/'
responce = requests.get(url)

content = responce.content.decode()
data = json.loads(content)

kurs = float(data[0]['Rate'])

amount = float(input("Dollor "))

result = kurs * amount
print(f"{result:,.2f}")