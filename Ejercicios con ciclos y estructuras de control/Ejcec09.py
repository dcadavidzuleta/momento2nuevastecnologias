def eliminarVocales(texto):
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    res = ""
    for letra in texto:
        if letra not in vocales:
            res += letra
    return res


texto = input("ingrese el texto\n")
print(eliminarVocales(texto))