from platform import AndroidVer, android_ver

lista = []
nombre = input("dame un nombre")
apodo = input("cual es tu apodo")
edad_input = input("cual es tu edad")
##validando edad si se deja vacio
if edad_input.strip().isdigit():
    edad = int(edad_input)
else:
    edad = 0
instruccion = input("cual es la instruccion")
if nombre != "" and apodo != "" and edad > 15 and instruccion == "configurar":
    animal = input("cual es el animal:")
    while animal != "":
        lista.append(animal)
        animal = input("Ingresa otro animal (o deja vacío para terminar): ")
    print("lista de animale", lista)

else:
    print(" debes ingresar todos los datos y cumplir con las condiciones (edad > 15 e instrucción = configurar")