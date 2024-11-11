# Crear y escribir en un archivo de texto
with open('archivo_texto.txt', 'w') as file:
    file.write("Este es un archivo de texto.\n")
    file.write("Podemos agregar varias líneas de texto.\n")

# Leer el contenido del archivo
with open('archivo_texto.txt', 'r') as file:
    contenido = file.read()
    print("Contenido del archivo de texto:")
    print(contenido)
