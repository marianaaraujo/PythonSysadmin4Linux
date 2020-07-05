lista = [] or list()
dicionario = {} or dict()
tupla = tuple()

lista_1 = [0,1,2,3,4,5,6,7,8,9]
print(lista_1)

lista_1.append(10)
print(lista_1)

for e in lista_1:
	print(e + 1)

print(lista_1[10])
print(lista_1[2])
#print(lista_1[11])

dicionario_1 = {'name': 'Mariana', 'age': 32, 'job':'System Analyst'}

print(dicionario_1['name'])
print(dicionario_1['age'])
print(dicionario_1['job'])

tuple_1 = (1,2,3,4)

print(tuple_1)

for e in tuple_1:
	print(e + 10)

lista_de_dicionarios = [
	{
		'name':'Mariana',
		'age': 32
	},
	{
		'name':'Bruno',
		'age': 35
	}
]

dicionario_de_listas = {
	'page':1,
	'index':[
		{
			'ch':1,
			'content':'lorem'

		}
	]
}

def fn(x,y,z):
	return x + y + z

print(fn(1,2,3))
print(fn(5,6,7))

resultado = fn(10,9,2)
print(resultado)

def g(x):
	return x ** 2, x / 2

x_quadrado, x_por_dois = g(2)
print(x_quadrado)

d = {'name':'Mariana', 'age':32}
d = ('Mariana', 32)