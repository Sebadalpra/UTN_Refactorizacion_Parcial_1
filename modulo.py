import os
import csv
import random

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

def guardar_csv(lista, nombre_archivo):
    """
    Guarda una lista de diccionarios en un archivo CSV con el mismo formato que el original
    
    Args:
        lista (list): Lista de diccionarios a guardar
        nombre_archivo (str): Nombre del archivo CSV
    """
    ruta = get_path_actual(nombre_archivo)

    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        encabezado = ['id', 'user', 'likes', 'dislikes', 'followers']
        esbribir_csv = csv.DictWriter(archivo, fieldnames=encabezado)
        esbribir_csv.writeheader()
        for post in lista:
            esbribir_csv.writerow(post)

    print(f"Archivo '{nombre_archivo}' guardado con éxito.")

# ----------------- MOSTRAR DATOS ----------------------------

def imprimir_lista(lista):
    for el in lista:
        print(el)

def asignar_valores_aleatorios(lista):
    for el in lista:
        el["likes"] = random.randint(300, 3000)
        el["dislikes"] = random.randint(300, 3500)
        el["followers"] = random.randint(10000, 20000)
    return lista

def filtrar_mejores_posts(lista):
    lista_filtrada = []
    for el in lista:
        if int(el["likes"]) > 2000:
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
    # ESTO ES UN MAX OR MIN FUNCIONAL Y GENERAL
    nuevo_elemento_max = int(lista[0][clave])
    nuevo_dict_max = lista[0]
    tam = len(lista)
    
    for i in range(1, tam):
        if funcion (nuevo_elemento_max, lista[i][clave]):
            nuevo_elemento_max = int(lista[i][clave])
            nuevo_dict_max = lista[i]

    return nuevo_dict_max