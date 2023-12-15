def mostrar_linea():
    ''' Esta función  pide al usuario 
    que ingrese dos números, n y m.

    Parámetros:
    Se utiliza with open() para abrir el fichero en modo lectura ('r').
    file.readlines() lee todas las líneas del fichero y las guarda en la lista lineas.

    Salida:
    Se verifica si los números ingresados (n y m)
    están dentro del rango permitido (1-10). Si alguno
    de los números está fuera de ese rango,
    se muestra un mensaje de error y la función termina.
    '''
    n = int(input("Escribe un número entre 1 y 10: "))
    m = int(input("Escribe otro número entre 1 y 10: "))

    if n < 1 or n > 10 or m < 1 or m > 10:
        print("Por favor, ingresa números entre 1 y 10.")
        return

    nombre_fichero = f"tabla-{n}.txt"

    with open(nombre_fichero, 'r') as file:
        lineas = file.readlines()
        if len(lineas) >= m:
            print(f"Línea {m}: {lineas[m - 1]}")
        else:
            print(f"El archivo no tiene {m} líneas.")

mostrar_linea()