def longitud_palabra():
    palabra = input("Ingrese una palabra: ")

    if len(palabra) < 4 :
        print("Hacen falta letras en la palabra")
    elif len(palabra) >= 4 and len(palabra) <= 8 :
        print("La palabra es correcta")
    elif len(palabra) > 8 :
        print("La palabra tiene " + str(len(palabra)) + " letras")

def encontrar_cuadrante():
    eje_x = int(input("Ingrese el eje x: "))
    eje_y = int(input("Ingrese el eje y: "))

    if eje_x == 0 and eje_y == 0:
        print("Origen del plano cartesiano")
    elif (eje_x > 0 and eje_y > 0):
        print("El punto se encuentra en el cuadrante I")
    elif (eje_y > 0 and eje_x < 0):
        print("El punto se encuentra en el cuadrante II")
    elif (eje_x < 0 and eje_y < 0):
        print("El punto se encuentra en el cuandrante III")
    elif (eje_x > 0 and eje_y < 0):
        print("El punto se encuentra en el cuadrante IV")

encontrar_cuadrante()
