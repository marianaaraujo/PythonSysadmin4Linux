import requests

route = "http://localhost:5000/users"

#response = requests.get(route)
#print(response.text)

#response = requests.patch(route + '/mariana')
#print(response.text)

payload = {
	'email': 'mari@teste.com.br',
	'password': 'secret'
}

response = requests.post(route, json=payload)
print(response.text)