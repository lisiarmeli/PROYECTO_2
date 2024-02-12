def longitud_palabra():
    palabra = input("Ingrese una palabra: ")

    if len(palabra) < 4 :
        print("Hacen falta letras en la palabra")
    elif len(palabra) >= 4 and len(palabra) <= 8 :
        print("La palabra es correcta")
    elif len(palabra) > 8 :
        print("La palabra tiene " + str(len(palabra)) + " letras")

longitud_palabra()