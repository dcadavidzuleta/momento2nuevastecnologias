lista = []

for i in range(10):
    valor = input ("# ingrese el número")
    lista.append(int(valor))

print ("la suma es ", sum(lista))
print ("el promedio es ", sum(lista) / len(lista))
print ("el menor es ", min(lista))
print ("el mayor es ", max(lista))