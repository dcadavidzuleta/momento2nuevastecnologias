def convertFarenheit(gradosCent):
    grados = gradosCent * 33.8
    return grados


grados = (float)(input("Ingrese la cantidad de grados centigrados\n"))
print("La cantidad en grados Farenheit es ", convertFarenheit(grados))