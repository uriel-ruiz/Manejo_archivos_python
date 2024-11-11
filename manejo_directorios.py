import os

# Crear un nuevo directorio
os.makedirs("nuevo_directorio", exist_ok=True)

# Listar el contenido de un directorio
print("Contenido del directorio actual:")
for elemento in os.listdir('.'):
    print(elemento)

# Cambiar el nombre de un archivo
if os.path.exists("archivo_texto.txt"):
    os.rename("archivo_texto.txt", "archivo_renombrado.txt")
    print("Archivo renombrado a 'archivo_renombrado.txt'")
