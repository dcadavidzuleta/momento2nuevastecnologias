seguir = 1
valores = []
continuar = 1


    def menores(lista):
        sum = 0
        for item in lista:
            if int(item) < 0:
                sum += 1
        return sum


    def mayores(lista):
        sum = 0
        for item in lista:
            if int(item) > 0:
                sum += 1
        return sum


    while int(seguir) == 1:
        valor = input("Ingrese cantidad\n")
        valores.append(valor)
        seguir = input("Si desea ingresar otra cantidad digite 1, sino digite 0\n")
    print("La cantidad de menores que 0 es", menores(valores))
    print("La cantidad de mayores que 0 es", mayores(valores))