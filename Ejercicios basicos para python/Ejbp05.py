valores = []

	for i in range(101):
	    if i % 2 == 0 and i > 0:
	        valores.append(int(i))
	        print(i)


	def multiplicar(lista):
	    mult = 1
	    for item in lista:
	        mult = mult * item
	    return mult


	print("La multiplicación de estos numeros es ", multiplicar(valores))