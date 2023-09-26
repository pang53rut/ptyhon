import requests
import json

ip = '192.168.14.86'

response = requests.get(f'https://ipapi.co/{ip}/json/')
result = response.json()

# Save the IP data to a JSON file
with open('ip_data.json','w') as file:
    json.dump(result, file)

print('IP data save to ip_data.json')

