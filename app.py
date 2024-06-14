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
9) Cargar archivo Json e imprimir los datos
10) Salir.
Requerimientos del desarrollo.
Nota 1: Todas las funciones deben estar en un módulo distinto al programa principal
y respetar las reglas de estilo de la cátedra.
Nota 2: Todas las funciones deben tener su propio docstring
Nota 3: Para ordenar se deberá utilizar los algoritmos de ordenamiento vistos en la catedra
"""

def main():
    print("""
        1. Cargar archivos CSV
        2. Imprimir lista
        3. Asignar estadísticas
        4. Filtrar por mejores posts
        5. Filtrar por haters
        6. Informar promedio de followers
        7. Ordenar los datos por nombre de user ascendente
        8. Mostrar más popular
        9. Salir
        """)
    
    flag_csv_cargado = False
    flag_datos_asignados = False

    while True:
        opcion = int(input("Ingrese una opción: "))
        match opcion:
            case 1:
                lista_original = cargar_csv("posts")
                flag_csv_cargado = True
            case 2:
                if flag_csv_cargado:
                    imprimir_lista(lista_original)
                else:
                    print("Primero debe cargar el CSV.")
            case 3:
                if flag_csv_cargado:
                    asignar_valores_aleatorios(lista_original)
                    flag_datos_asignados = True
                else:
                    print("Primero debe cargar el CSV.")
            case 4:
                if flag_csv_cargado:
                    if flag_datos_asignados:
                        nombre_archivo = input("Ingrese el nombre del archivo CSV de mejores posts: ")
                        lista_mejores_posts = si_es_mayor_o_menor(lista_original, lambda el: int(el["likes"]) > 2000)
                        guardar_csv(lista_mejores_posts, nombre_archivo)
                    else:
                        print("Antes debe asignarle datos al CSV.")
                else:
                    print("Primero debe cargar el CSV.")
            case 5:
                if flag_csv_cargado:
                    if flag_datos_asignados:                
                        lista_haters = si_es_mayor_o_menor(lista_original, lambda el: int(el["dislikes"]) > int(el["likes"]))
                        nombre_archivo = input("Ingrese el nombre del archivo para los haters: ")
                        guardar_csv(lista_haters, nombre_archivo)
                    else:
                        print("Antes debe asignarle datos al CSV.")
                else:
                    print("Primero debe cargar el CSV.")
            case 6:
                if flag_csv_cargado:
                    if flag_datos_asignados:
                        promedio(lista_original, "followers")
                    else:
                        print("Antes debe asignarle datos al CSV.")
                else:
                    print("Primero debe cargar el CSV.")
            case 7:
                if flag_csv_cargado:
                    if flag_datos_asignados:
                        lista_ordenada = burbujeo(lambda post1, post2: post1["user"] > post2["user"], lista_original)
                        nombre_archivo = input("Ingrese el nombre del archivo JSON: ")
                        guardar_json(lista_ordenada, nombre_archivo)
                    else:
                        print("Antes debe asignarle datos al CSV.")
                else:
                    print("Primero debe cargar el CSV.")
            case 8:
                if flag_csv_cargado:
                    if flag_datos_asignados:
                        dict_mas_popular = max_or_min(lista_original, "likes", lambda like1, like2: like1 < like2)
                        print(f"El usuario {dict_mas_popular["user"]} tiene el post mas likeado con {dict_mas_popular["likes"]}")
                    else:
                        print("Antes debe asignarle datos al CSV.")
                else:
                    print("Primero debe cargar el CSV.")
            case 9: #Cargar archivo Json e imprimir los datos
                nombre_archivo = input("Ingrese el nombre del archivo JSON: ")
                archivo_json = cargar_json(nombre_archivo)
                imprimir_lista(archivo_json)
            case 10:
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no valida.")

main()