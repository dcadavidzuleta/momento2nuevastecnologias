seguir = 1
edades = []
continuar = 1

def promediar(lista):
    sum = 0
    edMenores = 0
    for item in lista:
        if int(item) < 18:
            sum += int(item)
            edMenores += 1
    if edMenores == 0:
        return 0
    return sum / edMenores
            

while  int(continuar) == 1:
    while int(seguir) == 1:
        edad = input("Ingrese la edad del estudiante\n")
        edades.append(edad)
        seguir = input("Si desea ingresar otra edad ingrese 1, sino ingrese 0\n")
    print(promediar(edades))        
            
    continuar = input("Si desea ingresar nuevamente ingrese 1, sino ingrese 0\n")