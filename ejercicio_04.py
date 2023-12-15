import urllib.request

def contar_palabras(url):
    ''' Esta función accede al fichero de internet
    mediante la url.

    Parámetros:
    Utiliza urllib.request.urlopen(url) para abrir la URL 
    y obtener el contenido del archivo. Lee el contenido del fichero,
    divide y cuenta cuántas palabras hay en total.

    Salida:
    Devuelve el número total de palabras en el fichero, llama a la función
    y muestra el número de palabras por pantalla.
    '''
    operacion_exitosa = True
    
    # Obtener el contenido del archivo de texto desde la URL
    with urllib.request.urlopen(url) as file:
        contenido = file.read().decode('utf-8')
        
        # Contar las palabras en el texto
        palabras = contenido.split()
        num_palabras = len(palabras)
        
    if operacion_exitosa:
        return num_palabras
    else:
        print("No se pudo acceder al archivo.")
        return 0

# URL del fichero
url = "http://textfiles.com/adventure/aencounter.txt"

# Obtiene el número de palabras y muestra en pantalla
num_palabras = contar_palabras(url)
print(f"El número de palabras en el archivo es: {num_palabras}")