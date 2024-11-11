import zipfile

# Crear un archivo ZIP y agregar archivos
with zipfile.ZipFile('archivo.zip', 'w') as zip_ref:
    zip_ref.writestr('archivo_texto.txt', 'Contenido del archivo de texto dentro del ZIP.')
    zip_ref.writestr('archivo_binario.bin', b'Contenido binario en el archivo ZIP.')

# Leer el contenido de un archivo ZIP
with zipfile.ZipFile('archivo.zip', 'r') as zip_ref:
    print("Contenido del archivo ZIP:")
    for file in zip_ref.namelist():
        print(f"Archivo: {file}")
        with zip_ref.open(file) as f:
            print(f.read())
