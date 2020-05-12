def vueltas(radio, distancia):
    distanciaVuelta = 2 * 3.14 * radio
    cantidadVueltas = distancia / distanciaVuelta
    return cantidadVueltas
    
print("La cantidad de vueltas que da una rueda de 50 cm de diametro es ", vueltas(25, 100000))