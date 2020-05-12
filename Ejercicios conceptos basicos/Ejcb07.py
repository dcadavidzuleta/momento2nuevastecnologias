import math


def longitudSombra(gradosLuzSuelo: object, alturaEdificio: object) -> object:
    sombra = (math.sin(math.radians(90)) / math.sin(math.radians(gradosLuzSuelo)) * alturaEdificio)
    return sombra;


print("La longitud de la sombra de un edificio de 20m, si la luz y el suelo tienen un angulo de 22 grados es ",
      longitudSombra(22, 20))