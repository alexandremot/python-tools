
import requests

url = "http://18.231.152.211:5000/pedidos"
payload=""
headers = {'Content-Type': 'application/json'}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)
