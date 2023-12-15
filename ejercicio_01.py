def guardar_tabla():
    ''' Esta funcion pide un numero entero 
    entre 1 y 10 y verifica si el numero ingresado
    está dentro del rango.
    Parametros: 
    Crea un fichero con el nombre de ¨tabla-n.txt¨
    donde ¨n¨ es el numero ingresado.
    Dentro del fichero escribe la tabla de multiplicar del numero
    que se ingresó.
    Salida:
    En caso de escribir otro numero que no está en el rango,
    este comando lo rechazará.
    else:
        print()'''
    
    numero = int(input("Escribe un numero entero entre 1 y 10: "))
    if 1 <= numero <= 10:
        with open("tabla- " + str(numero) + ".txt", "w") as file:
            file.write("Tabla de multiplicar del " + str(numero) + ":\n")
            for i in range(1, 11):
                resultado = numero * i
                file.write(str(numero) + " x " + str(i) + " = " + str(resultado) + "\n")
        print("La tabla de multiplicar del " + str(numero) + 
              " ha sido guardada en tabla-del-" + str(numero) + ".txt")
    else:
        print()
guardar_tabla()