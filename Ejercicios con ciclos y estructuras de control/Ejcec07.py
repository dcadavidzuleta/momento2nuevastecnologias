vocales = ["a", "e", "i", "o", "u"]


def dividirEnLetras(texto):
    return [char for char in texto]


def contarVocales(texto):
    lista = dividirEnLetras(texto)
    dic = {}
    for vocal in vocales:
        dic[vocal] = lista.count(vocal)
    return dic


texto = input("ingrese el texto")
print(contarVocales(texto))