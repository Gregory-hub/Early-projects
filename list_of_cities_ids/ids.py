import json

with open('C:\Gry\Files\list_of_cities_ids\city_ids.json', 'rb+') as file:
    cities = json.load(file)

print(cities[100]['name'] + ':', cities[100]['id'])
