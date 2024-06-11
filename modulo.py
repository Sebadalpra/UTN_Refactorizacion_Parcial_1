import os
import csv
import random
import json

# ----------- CSV -----------------

def get_path_actual(nombre_archivo: str) -> str:
    """
    Devuelve la ruta completa del archivo en el directorio actual
    
    Args:
        nombre_archivo (str): Nombre del archivo
        
    Returns:
        str: Ruta completa del archivo
    """
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def cargar_csv(nombre_archivo: str) -> list:
    """
    Carga un archivo CSV en una lista de diccionarios
    
    Args:
        nombre_archivo (str): Nombre del archivo CSV a cargar
        
    Returns:
        list: Lista de diccionarios con los datos del CSV
    """
    ruta = get_path_actual(nombre_archivo)
    lista_posts = []
    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista_posts.append(fila)
        print("Archivo cargado con éxito.")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.") 
    return lista_posts

def guardar_csv(lista: list, nombre_archivo: str) -> csv:
    """
    Guarda una lista de diccionarios en un archivo CSV con el mismo formato que el original
    
    Args:
        lista (list): Lista de diccionarios a guardar en un CSV
        nombre_archivo (str): Nombre del archivo CSV a guardar
    
    Returns:
        csv: Un archivo CSV con los datos de la lista dada
    """
    ruta = get_path_actual(nombre_archivo)

    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        encabezado = ['id', 'user', 'likes', 'dislikes', 'followers']
        esbribir_csv = csv.DictWriter(archivo, fieldnames=encabezado)
        esbribir_csv.writeheader()
        for post in lista:
            esbribir_csv.writerow(post)

    print(f"Archivo '{nombre_archivo}' guardado con éxito.")

# ------------------- JSON --------------------------------

def guardar_json(lista: list, nombre_archivo: str) -> json:
    """
    Guarda una lista de diccionarios en un archivo JSON

    Args:
        lista (list): Lista de diccionarios a guardar en un JSON
        nombre_archivo (str): Nombre del archivo JSON a guardar

    Returns:
        json: Un archivo JSON con los datos de la lista dada.
    """

    ruta = get_path_actual(nombre_archivo)
    
    with open(ruta, "w", encoding = "utf-8") as archivo:

        # Convertir el codigo Python en formato JSON
        json.dump(lista, archivo, ensure_ascii=False, indent=4)

    print(f"Archivo guardado en: {ruta}")

# ----------------- MOSTRAR DATOS ----------------------------

def imprimir_lista(lista: list) -> None:
    print("LISTA")
    print(f"{'ID':<20} {'USER':<20} {'LIKES':<30} {'DISLIKES':<30} {'FOLLOWERS':<40}")
    print("-" * 140)
    for dict in lista:
        # Una vez q accedo al nivel del diccionario lo paso a otro funcion en donde voy por sus elementos
        mostrar_datos(dict)

def mostrar_datos(dict: dict) -> str:
    print(f"{dict['id']:<20} {dict['user']:<20} {dict['likes']:<30} {dict['dislikes']:<30} {dict['followers']:<40}")

# ----------------- FUNCIONES --------------------------------

def asignar_valores_aleatorios(lista: list) -> list:
    """ 
    Asigna una lista de valores a una lista de diccionarios.

    Args:
        lista (_type_): Lista de diccionarios a alterar.

    Returns:
        _type_: La lista con los datos modificados.
    """
    for el in lista:
        el["likes"] = random.randint(300, 3000)
        el["dislikes"] = random.randint(300, 3500)
        el["followers"] = random.randint(10000, 20000)
    return lista

def filtrar_mejores_posts(lista: list, funcion) -> list:
    lista_filtrada = []
    for el in lista:
        if funcion(el):
            lista_filtrada.append(el)
    return lista_filtrada

def haters(lista, clave1, clave2):
    lista_filtrada = []
    for el in lista:
        if int(el[clave1]) > int(el[clave2]):
            lista_filtrada.append(el)
    return lista_filtrada

def promedio(lista, clave):
    suma = 0
    tam = len(lista)
    for el in range(tam):
        suma += lista[el][clave]

    resultado_promedio = suma / tam
    print(f"El promedio de {clave} es: {resultado_promedio}")

def mas_popular(lista, clave, funcion):
    # MAX OR MIN FUNCIONAL Y GENERAL
    nuevo_elemento_max = int(lista[0][clave])
    nuevo_dict_max = lista[0]
    tam = len(lista)
    
    for i in range(1, tam):
        if funcion (nuevo_elemento_max, lista[i][clave]):
            nuevo_elemento_max = int(lista[i][clave])
            nuevo_dict_max = lista[i]

    return nuevo_dict_max

def burbujeo(funcion, lista: list):
    # Esto al no estar mapeando una lista, modifica la lista original.

    tam = len(lista)
    
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            # voy a recibir luego por la funcion lambda en x lo que esta en lista[i] y a ese diccionario que recibo le agrego ["user"], lo mismo con j
            if funcion(lista[i], lista[j]):
                # swap
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista