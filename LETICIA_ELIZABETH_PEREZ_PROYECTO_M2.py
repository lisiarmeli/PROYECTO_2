def longitud_palabra():
    palabra = input("Ingrese una palabra: ")

    if len(palabra) < 4:
        print("Hacen falta letras en la palabra")
    elif len(palabra) >= 4 and len(palabra) <= 8:
        print("La palabra es correcta")
    elif len(palabra) > 8:
        print("La palabra tiene " + str(len(palabra)) + " letras")


def encontrar_cuadrante():
    eje_x = validar_coordenada(input("Ingrese el eje x: "))
    while eje_x == 0:
        eje_x = validar_coordenada(int(input("Ingrese una cordenada valida para X: ")))
    else:
        eje_y = validar_coordenada(int(input("Ingrese el eje y: ")))
        while eje_y == 0:
            eje_x = validar_coordenada(int(input("Ingrese una cordenada valida para Y: ")))


    if (eje_x > 0 and eje_y > 0):
        print("El punto se encuentra en el cuadrante I")
    elif (eje_y > 0 and eje_x < 0):
        print("El punto se encuentra en el cuadrante II")
    elif (eje_x < 0 and eje_y < 0):
        print("El punto se encuentra en el cuandrante III")
    elif (eje_x > 0 and eje_y < 0):
        print("El punto se encuentra en el cuadrante IV")


def validar_coordenada(coordenada):
    try:
        valida = int(coordenada)
        if valida == 0:
            return 0
        else:
            return valida
    except ValueError:
        return 0


longitud_palabra()

encontrar_cuadrante()
