import random

class Adivinumero:
	ganador = False

	def __init__(self, numero, intentos = 5):
		self.numero = numero
		self.intentos = intentos

	def getNumero(self):
		return self.numero

	def getIntentos(self):
		return self.intentos
	
	def adivinar(self, numero):
		if (numero == self.numero):
			print("Adivinaste!\n")
			self.ganador = True
		elif (self.numero > numero):
			print("El número es MAYOR a %i" % (numero))
			self.descontarIntentos()
		else:
			print("El número es MENOR a %i" % (numero))
			self.descontarIntentos()

	def darPista(self):
		pista = random.randint(30,70)
		if ( pista == self.getNumero() ):
			pista += 1
		self.adivinar(pista)
		self.descontarIntentos()

	def descontarIntentos(self):
		self.intentos -= 1


def verificarNum():
	correcto = True
	while correcto:
		try:		
			valor = int(valor)
			correcto = False
		except Exception as error:
			valor = input('\tIngresaste un valor erroneo. Vuelve a intentar: ')