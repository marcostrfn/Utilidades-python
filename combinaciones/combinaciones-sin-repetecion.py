#!/usr/bin/python


caracteres = "abc"
elementos_combinacion = 3
posicion = [0] * elementos_combinacion

def imprimir(caracteres, posicion, elementos_combinacion):	
	# si hay elementos iguales en posicion ej = [0,1,0]
	# no imprimimos la cadena
	for x in range(0,len(caracteres)-1):
		for y in range(x+1,len(caracteres)):
			if posicion[x]==posicion[y]:
				return
				
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
			
	
	
