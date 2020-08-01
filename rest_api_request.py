import json
import requests

response = requests.get('https://viacep.com.br/ws/01309-010/json/')
todos = json.loads(response.text)

print(todos)