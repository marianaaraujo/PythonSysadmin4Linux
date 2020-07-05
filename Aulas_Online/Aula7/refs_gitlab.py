import requests
import json

token = "abc123"

#projetos = requests.get("http://192.168.0.100/api/v4/projects?private_token=%s"%(token))
#print(projetos)
#print(
#	json.dumps(
#		projetos.json(),
#		indent=4, sort_keys=True
#	)
#)

#data = {
#	"name": "flask-app"
#}

#projeto = requests.post("http://192.168.0.100/api/v4/projects?private_token=%s"%(token),data)
#print(projeto.json())

#usuarios = requests.get("http://192.168.0.100/api/v4/users?private_token=%s"%(token))
#print(usuarios.json())
#print(
#	json.dumps(
#		usuarios.json(),
#		indent=4, sort_keys=True
#	)
#)

#data = {
#	"name": "mari@teste.com.br",
#	"username": "mari.teste",
#	"name": "Mari Teste",
#	"password": "4linux123"
#}

#usuario = requests.post("http://192.168.0.100/api/v4/users?private_token=%s"%(token),data)
#print(projeto.json())

#project_id = 4
#data = {
#	"user_id":2,
#	"access_level":40
#}
#projeto = requests.post("http://192.168.0.100/api/v4/projects/members?private_token=%s"%(project_id, token),data)
print(projeto.json())
