import random

from clases import Adivinumero

print("\n 	-------------------------")
print(" 	Bienvenidos a Adivinumero")
print(" 	-------------------------\n")

numero = random.randint(0,100)
intentos = 5

juego = Adivinumero(numero, intentos)

while ( juego.getIntentos() > 0 and not juego.ganador ):
	numero = input("\nIngrese un número: ['P' para pedir Pista]: ")
	if (numero.upper() == 'P'):
		juego.darPista()
	elif (numero == 'nopuedoconlavida'):
		print ("Lo sé, dejá de llorar. El número es %i " %(juego.getNumero()))
	elif numero.isdigit():
		numero =int(numero)

		# Adivinar el Número!
		if (numero == juego.getNumero()):
			print("Adivinaste!\n")
			juego.ganador = True
		elif (juego.getNumero() > numero):
			print("El número es MAYOR a %i" % (numero))
			juego.descontarIntentos()
		else:
			print("El número es MENOR a %i" % (numero))
			juego.descontarIntentos()

	else:
		print ("	Error: ingreso inválido.")

if not juego.ganador:
	print("\nPerdiste =(\n")
print ("\nGracias por jugar ;)\n")

			