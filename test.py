import os
import requests
import json

response = requests.get('http://api.openweathermap.org/data/2.5/weather?id={0}&appid={1}'.format(2643743, '4dfe4b7edb45aecd040d4ea6b542f4b3'))
response_text = json.loads(response.text)
print(response_text)
