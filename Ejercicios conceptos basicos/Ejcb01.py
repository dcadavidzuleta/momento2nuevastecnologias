def area(base, altura):
    area = (base * altura) / 2
    return area


base = (int)(input("Ingrese el tamaño de la base\n"))
altura = (int)(input("ingrese el tamaño de la altura\n"))
print("El area del triangulo es ", area(base, altura))