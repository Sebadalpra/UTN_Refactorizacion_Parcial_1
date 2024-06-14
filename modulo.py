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

def cargar_csv(nombre_archivo: str):
    ruta = get_path_actual(nombre_archivo + ".csv")
    with open(ruta) as archivo:
        lista_posts = []

        # Encabezado en lista

        encabezado = archivo.readline().strip("\n").split(",")

        # Contenido en lista
        for linea in archivo.readlines():

            dict_posts = {}

            linea = linea.strip("\n").split(",")

            # Asigna cada valor de la lista linea a las variables id, nombre, apellido, edad, correo y direccion.
            id,user,likes,dislikes,followers = linea

            dict_posts["id"] = int(id)
            dict_posts["user"] = user
            dict_posts["likes"] = int(likes)
            dict_posts["dislikes"] = int(dislikes)
            dict_posts["followers"] = int(followers)
            lista_posts.append(dict_posts)

    print(f"Archivo {nombre_archivo} cargado con éxito.")

    return lista_posts

def guardar_csv(lista, nombre_archivo) -> csv:
    """
    Guarda una lista de diccionarios en un archivo CSV con el mismo formato que el original
    
    Args:
        lista (list): Lista de diccionarios a guardar en un CSV
        nombre_archivo (str): Nombre del archivo CSV a guardar
    
    Returns:
        csv: Un archivo CSV con los datos de la lista dada
    """
    ruta = get_path_actual(nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as archivo_modificado:
        dato = csv.writer(archivo_modificado)

        # ESCRIBO EL ENCABEZADO
        encabezado = ['id', 'user', 'likes', 'dislikes', 'followers']
        dato.writerow(encabezado)

        # Que hay dentro de lista? diccionarios, entonces recorro cada uno de ellos usando dict_persona y se agregan como campos
        for dict_post in lista:
            dato.writerow([
                dict_post["id"],
                dict_post["user"],
                dict_post["likes"],
                dict_post["dislikes"],
                dict_post["followers"],
                ])

    print(f"Archivo modificado se encuntra en: {ruta}")

# ------------------- JSON --------------------------------

def cargar_json(nombre_archivo):

    ruta = get_path_actual(nombre_archivo + ".json")

    with open(ruta,"r",encoding = "utf-8") as archivo:

        # Verifico que haya abierto. Si está en false es porque aun no se cerró
        print(f"{archivo.closed}")   

        # Cargo el archivo que hace referencia a la ruta y lo guardo en la variable.
        # Me genera una lista de diccionarios.
        posts_json = json.load(archivo)

    return posts_json

def guardar_json(lista: list, nombre_archivo: str) -> json:
    """
    Guarda una lista de diccionarios en un archivo JSON

    Args:
        lista (list): Lista de diccionarios a guardar en un JSON
        nombre_archivo (str): Nombre del archivo JSON a guardar

    Returns:
        json: Un archivo JSON con los datos de la lista dada.
    """

    ruta = get_path_actual(nombre_archivo + ".json")
    
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
        mostrar_datos(dict)

def mostrar_datos(dict: dict) -> str:
    print(f"{dict['id']:<20} {dict['user']:<20} {dict['likes']:<30} {dict['dislikes']:<30} {dict['followers']:<40}")

# ----------------- FUNCIONES GENERALES --------------------------------

def asignar_valores_aleatorios(posts: list) -> None:
    """ 
    Asigna una lista de valores a una lista de diccionarios.

    Args:
        lista (_type_): Lista de diccionarios a alterar.
    """
    for el in posts:
        el["likes"] = random.randint(300, 3000)
        el["dislikes"] = random.randint(300, 3500)
        el["followers"] = random.randint(10000, 20000)

    print(f"Valores asignados correctamente")

def si_es_mayor_o_menor(lista: list, funcion) -> int:
    """ Conseguir un valor que sea mayor o menor al segundo valor.

    Args:
        lista (list): Lista a mapear
        funcion (_type_): Determina que un valor sea mayor o menor al segundo valor

    Returns:
        int: Retorna un entero > o < al segundo valor, según lo establecido en la función.
    """
    lista_filtrada = []
    for el in lista:
        if funcion(el):
            lista_filtrada.append(el)
    return lista_filtrada

def promedio(lista: list, clave: str) -> None:
    """ Establece un promedio de números en una lista de diccionarios.

    Args:
        lista (list): Lista de diccionarios con los datos a usar.
        clave (str): Clave que contiene un valor numérico
    """
    suma = 0
    tam = len(lista)
    for el in range(tam):
        suma += lista[el][clave]

    resultado_promedio = suma / tam
    print(f"El promedio de {clave} es: {resultado_promedio}")

def max_or_min(lista: list, clave: str, funcion) -> dict:
    """ Calcula el maximo o minimo de una lista de diccionarios.

    Args:
        lista (list): Lista de diccionarios.
        clave (str): Clave del diccionario para acceder al valor del elemento.
        funcion (_type_): Compara un valor con otro estableciendo un > o <.

    Returns:
        dict: Retorna un diccionario con el valor maximo o minimo.
    """
    # MAX OR MIN FUNCIONAL Y GENERAL
    nuevo_elemento_max = int(lista[0][clave])
    nuevo_dict_max = lista[0]
    tam = len(lista)
    
    for i in range(1, tam):
        if funcion (nuevo_elemento_max, lista[i][clave]):
            nuevo_elemento_max = int(lista[i][clave])
            nuevo_dict_max = lista[i]

    return nuevo_dict_max

def burbujeo(funcion, lista: list) -> list:
    """ Ordenar una lista en orden ascendente o descendente.

    Args:
        funcion (_type_): Compara dos valores establenciendo una condición > o < para determinar si el orden es asc o desc.
        lista (list): Lista a ordenar.
    """

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