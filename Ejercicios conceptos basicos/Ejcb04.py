def lustroSegundos(lustros):
    segundos = lustros * 5 * 365 * 24 * 60 * 60
    return segundos


lustros = (float)(input("Ingrese la cantidad de lustros\n"))
print("La cantidad de segundos es ", lustroSegundos(lustros))