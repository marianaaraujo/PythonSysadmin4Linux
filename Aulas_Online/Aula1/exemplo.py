import requests

data = {
	"nome": "mariana",
	"sobrenome": "araujo"
}

requisicao = requests.delete("http://httpbin.org/delete", json=data)

json_to_dict = requisicao.json()
print(json_to_dict)