def obtener_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

lista = [-25, 12, 32, 44.67,9,12,100, -33, -10]
pares = obtener_pares(lista)
print(pares)

