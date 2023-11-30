import json

# Nombre del archivo JSON
archivo_json = 'scores.json'

# Función para cargar los datos del archivo JSON a un diccionario
def cargar_datos_json():
    try:
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
    except FileNotFoundError:
        return {}
    return datos

# Función para actualizar el diccionario con nuevos datos
def actualizar_diccionario(diccionario, nuevos_datos):
    diccionario.update(nuevos_datos)

# Función para guardar los datos actualizados en el archivo JSON
def guardar_datos_json(datos, nuevos_datos):

    actualizar_diccionario(datos, nuevos_datos)

    with open(archivo_json, 'w') as file:
        json.dump(datos, file, indent=4)
