from modulo import *

""" 
1) Cargar archivo CSV: Se pedirá el nombre del archivo y se cargará en una lista de diccionarios
los elementos del mismo. Informar que se ha cargado con éxito.
2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de los posts.
3) Asignar estadísticas: Se deberá mapear la lista con una función que asignará a cada post un
valor de likes entre 500 y 3000, dislikes con valores entre 300 y 3500 y followers entre 10000 y
20000. calculados de manera aleatoria.
4) Filtrar por mejores posts: Se deberá generar un archivo igual al original, pero donde solo
aparezcan los posts con más de 2000 likes.
5) Filtrar por haters: Se deberá generar un archivo igual al original, pero donde solo aparezcan
posts donde la cantidad de dislikes supere a la de likes.
6) Informar promedio de followers: Informar por consola el promedio de followers.
7) Ordenar los datos por nombre de user ascendente: Se deberán ordenar los datos y al listado
ordenado guardarlo en un archivo en formato JSON.
8) Mostrar más popular: Informar el nombre del user o users con el posteo más likeado. Y cuál es
ese número.
9) Salir.
Requerimientos del desarrollo.
Nota 1: Todas las funciones deben estar en un módulo distinto al programa principal
y respetar las reglas de estilo de la cátedra.
Nota 2: Todas las funciones deben tener su propio docstring
Nota 3: Para ordenar se deberá utilizar los algoritmos de ordenamiento vistos en la catedra
"""

def main():
    print("""
        1. Cargar archivos CSV
          
          """)
    
    while True:
        opcion = int(input("Ingrese una opción: "))
        match opcion:
            case 1:
                nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
                lista_original = cargar_csv(nombre_archivo)
            case 2:
                imprimir_lista(lista_original)
            case 3:
                lista_modificada = asignar_valores_aleatorios(lista_original)
            case 4:
                nombre_archivo = input("Ingrese el nombre del archivo CSV de mejores posts: ")
                # utilizo la lista nueva generada en el case 3 ()
                lista_mejores_posts = filtrar_mejores_posts(lista_modificada)
                guardar_csv(lista_mejores_posts, nombre_archivo)
            case 5:
                lista_haters = haters(lista_modificada, "dislikes", "likes")
                nombre_archivo = input("Ingrese el nombre del archivo para los haters: ")
                guardar_csv(lista_haters, nombre_archivo)
            case 6:
                promedio_followers = promedio(lista_modificada, "followers")
            case 7:
                pass
            case 8:
                dict_mas_popular = mas_popular(lista_modificada, "likes", lambda a, b: a < b)
                print(f"El usuario {dict_mas_popular["user"]} tiene el post mas likeado con {dict_mas_popular["likes"]}")







main()





""" 
            case "1":
                nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
                lista_posts = modulo.cargar_csv(nombre_archivo)
            case "2":
                modulo.imprimir_lista(lista_posts)
            case "3":
                lista_posts = modulo.asignar_estadisticas(lista_posts)

                En case 1 cargo el csv en la variable lista_post
                luego en case 3 asigno nuevas valores y piso la variable anterior lista_post con lo cual estoy reemplazando los valores
                Estos valores reemplazados no se van a ver reflejados en el orignial (posts.csv), ya que para eso deberia entrar al case 4 y guardar el csv con el mismo nombre que el archivo original, es decir posts.csv en ese caso reemplazaria sus valores

                # en el case 2 no se ve como una lista de diccionarios ya que recorri esa lista con imprimir_lista

                # sin embargo, trabajo con una lista de diccionarios
                Por ello tengo que hacer siempre for post in lista (para acceder uno x uno a cada diccionario de la lista
                Entonces Ej. post["likes"]) -> accedo a los likes, es decir su valor a traves de su clave



                # EXPLICACION SOBRE PORQUE SE GENERA DESDE UN PRINCIPIO UNA LISTA DE DICCIONARIOS:
                SECCION DE CARGAR_CSV

                with open(ruta, mode="r", encoding="utf-8") as archivo:
                    lector = csv.DictReader(archivo)
                    for fila in lector:
                        lista_posts.append(fila)

                Aquí, el archivo CSV se abre en modo lectura (mode="r") con codificación UTF-8. csv.DictReader se usa para leer el archivo CSV y convertir cada fila en un diccionario. Cada fila del CSV se añade a la lista lista_posts.
"""