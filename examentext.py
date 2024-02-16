import sys
##    hacemos el menu
def menu():
    print("Elige una opción:")
    print("1.-Listado de libros")
    print("2.-Buscar de libros")
    print("3.-Insertar nuevos libros")
    print("4.-Actualizar libros")
    print("5.-Eliminar libros")
    print("6.-Salir")
    opcion = input("Opción: ")
##    con los if y los elif vamos creando las peticiones
    if opcion == "1":
        print("Listamos los libros")
        archivo = open("libros.txt",'r')
        contenido = archivo.readlines()
        for fila in contenido:
            print(fila)
        archivo.close()
    elif opcion == "2":
        print("Buscamos un libro")
        criterio = input("Introduce tu criterio de busqueda")
        archivo = open("libros.txt",'r')
        contenido = archivo.readlines()
        for fila in contenido:
            if criterio.lower() in fila.lower():
                print(fila)
        archivo.close()
    elif opcion == "3":
        print("Insertamos un libro")
        titulo = input("Introduce el titulo del libro:")
        autor = input("Introduce el autor del libro:")
        anio = input("Introduce el año de publicacion:")
        editorial = input("Introduce la editorial del libro:")
        sinopsis = input("Introduce la sinopsis del libro:")
        s = ","
        nl = "\n"
        archivo = open("libros.txt",'a')
        archivo.write(titulo+s+autor+s+anio+s+editorial+sinopsis+nl)
        archivo.close()
    elif opcion == "4":
        print("Actualizamos un libro")
        criterio = input("Introduce la entrada a actualizar")
        titulo = input("Introduce el titulo del libro:")
        autor = input("Introduce el autor del libro:")
        anio = input("Introduce año de publicación:")
        editorial = input("Introduce la editorial:")
        sinopsis = input("Introduce la sinopsis del libro:")
        # abro el archivo libros
        archivo = open("libros.txt",'r')
        contenidoinicio = archivo.readlines()
        contenidofinal = []
        # busco linea a linea algo que coincida con la entrada a actualizar
        for fila in contenidoinicio:
            if criterio.lower() in fila.lower():
                s = ","
                nl = "\n"
                contenidofinal.append(titulo+s+autor+s+anio+s+editorial+sinopsis+nl)
            else:
                contenidofinal.append(fila) #lo agrego
        archivo.close()
        # abro el archivo pero en modo w
        archivo = open("libros.txt",'w')
        #repaso el contenido final
        for fila in contenidofinal:
            archivo.write(fila) #escribo en el archivo
        archivo.close() # cierro el archivo
    elif opcion == "5":
        print("Eliminamos un registro")
        criterio = input("Introduce la entrada a eliminar")
        # abro el archivo original
        archivo = open("libros.txt",'r')
        contenidoinicio = archivo.readlines()
        contenidofinal = []
        # busco linea a linea
        for fila in contenidoinicio:
            if criterio.lower() in fila.lower():
                pass # si un elemento coincide con la busqueda, no lo agrego
            else:
                contenidofinal.append(fila) #lo agrego
        archivo.close()
        # abro el archivo pero en modo w
        archivo = open("libros.txt",'w')
        #repaso el contenido final
        for fila in contenidofinal:
            archivo.write(fila) #escribo en el archivo
        archivo.close() # cierro el archivo
    elif opcion == "6":
        print("Salimos")
        sys.exit()
    menu()

menu()
