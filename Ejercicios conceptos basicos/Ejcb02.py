def convertPesos(dolares):
    pesos = dolares * 3827.57
    return pesos


dolares = (float)(input("Ingrese la cantidad de dolares\n"))
print("El valor en COP es ", convertPesos(dolares))