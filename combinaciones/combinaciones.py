#!/usr/bin/python


caracteres = ['0','1','2','3','4','5','6','7','8','9',
	'A','B','C','D','E','F','G','H','I','J','K','L','M',
	'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
	'a','b','c','d','e','f','g','h','i','j','k','l','m',
	'n','o','p','q','r','s','t','u','v','w','x','y','z']

elementos_combinacion = 20
posicion = [0] * elementos_combinacion

def imprimir(caracteres, posicion, elementos_combinacion):
	# print posicion,
	for x in range(0,elementos_combinacion):
		print caracteres[posicion[x]],

	print

def combinar(caracteres, posicion, elementos_combinacion):
	for i in range(0, len(caracteres)):
		imprimir(caracteres, posicion, elementos_combinacion)
		posicion[elementos_combinacion - 1] += 1


while True:
	for x in range(elementos_combinacion - 1, 0, -1):
		if posicion[x] == len(caracteres):
			posicion[x] = 0
			posicion[x-1] += 1

	if posicion[0] == len(caracteres):
		break

	combinar(caracteres,posicion, elementos_combinacion)
	for x in range(0,elementos_combinacion,4):
		print x, caracteres[posicion[x]], caracteres[posicion[x+1]],caracteres[posicion[x+2]],caracteres[posicion[x+3]]

	break




