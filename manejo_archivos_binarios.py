# Crear un archivo binario escribiendo bytes
with open('archivo_binario.bin', 'wb') as file:
    file.write(b'Este es un archivo binario.\n')
    file.write(b'Incluye contenido en formato binario.\n')

# Leer el archivo binario
with open('archivo_binario.bin', 'rb') as file:
    contenido = file.read()
    print("Contenido del archivo binario:")
    print(contenido)
