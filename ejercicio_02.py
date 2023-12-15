import os

def mostrar_tabla():
    '''  Esta función solicita al usuario que 
    introduzca un número entero entre 1 y 10 y
    lea el fichero tabla-n.txt con la tabla de
    multiplicar de ese número

    Parámetros:
    Verificación de la existencia del fichero: Utilizamos
    el código os.listdir() para obtener un listado de los archivos.
    Comprobamos la existencia del fichero deseado,
    El código verifica si el fichero (tabla- .txt) está en la lista 
    actual usando el carácter "in".

    Salida:
    Si el archivo existe en el fichero, el código lo abre,
    lee su contenido (la tabla de multiplicar)
    y lo muestra. Si el archivo no existe, 
    el programa muestra un mensaje que no se encontró el fichero.
    '''

    numero = int(input("Escribe un número entero entre 1 y 10: "))
    if numero < 1 or numero > 10:
        print("No es un numero entre 1 y 10.")
        return

    nombre_fichero = "tabla- " + str(numero) + ".txt"
    fichero = os.listdir()
    if nombre_fichero in fichero:
        with open(nombre_fichero, 'r') as archivo:
            tabla = archivo.read()
            print("Tabla- " + str(numero) + ":\n" + tabla)
    else:
        print("El archivo " + nombre_fichero + " no existe.")

mostrar_tabla()