import xml.etree.ElementTree as ET

# Crear y guardar un archivo XML
root = ET.Element("datos")
persona = ET.SubElement(root, "persona")
persona.set("nombre", "Juan")
ET.SubElement(persona, "edad").text = "30"
ET.SubElement(persona, "ciudad").text = "Ciudad Ejemplo"
tree = ET.ElementTree(root)
tree.write("archivo.xml")

# Leer el archivo XML
tree = ET.parse("archivo.xml")
root = tree.getroot()
print("Contenido del archivo XML:")
for elem in root:
    print(f"Persona: {elem.attrib['nombre']}, Edad: {elem.find('edad').text}, Ciudad: {elem.find('ciudad').text}")
