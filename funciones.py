from random import shuffle


def configurar_juego():
    print("funcion para configurar la lista de animales")
    animales = []
    while True:
        animal = input(" dame un animal: ")
        if animal.lower() == "q":
            exit()
        elif animal.lower() == "jugar":
            break
        else:
            animales.append(animal)
    return animales


def elegir_animal(animales):
    shuffle(animales)
    return animales[0]


def adivinar(animales):
    elegido = elegir_animal(animales)
    print("\nHora de adivinar")
    print("\nanimales en el juego", animales)
    print("escribe q para salir en cualquier momento. \n")

    while True:
        intento = input("que animal crees que elegi")
        if intento.lower() == "q":
            exit()
        elif intento.lower() == elegido.lower():
            print("Has ganado")
            break
        else:
            print("No as acertado. Intenta de nuevo.")

            if __name__ == "__main__":
                animales = configurar_juego()
                adivinar(animales)
# Este bloque permite usar funciones sin que se ejecute el juego automáticamente si lo importas
if __name__ == "__main__":
    animales = configurar_juego()
    adivinar(animales)