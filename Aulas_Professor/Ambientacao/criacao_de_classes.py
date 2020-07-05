class User:
	
	def __init__(self,name):
		self.name = name

	def say_hello(self):
		print('hello, my name is '+self.name)

class PaulistaUser(User):

	def say_hello(self):
		print('e ai mano, beleza? Sou o(a) '+self.name)

class CariocaUser(User):

	def say_hello(self):
		print('fala ae peixe,  '+self.name)

user_1 = User('Mariana')
user_2 = PaulistaUser('Bruno')
user_3 = User('Ana')
user_4 = CariocaUser('Julio')

user_1.say_hello()
user_2.say_hello()
user_3.say_hello()
user_4.say_hello()

