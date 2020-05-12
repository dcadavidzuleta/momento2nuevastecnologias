valores = []

for i in range(10):
    valor = input("ingrese valor\n")
    valores.append(int(valor))


def sumar(lista):
    sum = 0
    for valor in range(len(lista) + 1):
        sum += valor
    return sum


print("la suma es ", sumar(valores))