    valores = []


    def fibonacci(actual, cantidad):
        index = actual
        while (index < cantidad):
            if index == 0:
                numeros.append(0)
            elif index == 1:
                numeros.append(1)
            else:
                numeros.append(numeros[actual - 1] + numeros[index - 2])
            index += 1


    def imprimir(lista):
        for i in lista:
            print(i)


    cantidad = input("Cuantos numeros desea generar?\n")
    fibonacci(0, int(cantidad))
    imprimir(numeros)