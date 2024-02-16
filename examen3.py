import sys

def menu():
    print("Elige una opción:")
    print("1.-Listado de registros")
    print("2.-Buscar registros")
    print("3.-Insertar registros")
    print("4.-Actualizar registros")
    print("5.-Eliminar registros")
    print("6.-Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        print("Listamos los registros")
        archivo = open("datos.txt",'r')
        contenido = archivo.readlines()
        for fila in contenido:
            print(fila)
        archivo.close()
    elif opcion == "2":
        print("Buscamos un registro")
        criterio = input("Introduce tu criterio de busqueda")
        archivo = open("datos.txt",'r')
        contenido = archivo.readlines()
        for fila in contenido:
            if criterio.lower() in fila.lower():
                print(fila)
        archivo.close()
    elif opcion == "3":
        print("Insertamos un registro")
        titulo = input("Introduce el titulo de la web:")
        descripcion = input("Introduce la descripción de la web:")
        url = input("Introduce la url de la web:")
        categoria = input("Introduce la categoría de la web:")
        s = ","
        nl = "\n"
        archivo = open("datos.txt",'a')
        archivo.write(titulo+s+descripcion+s+url+s+categoria+nl)
        archivo.close()
    elif opcion == "4":
        print("Actualizamos un registro")
        criterio = input("Introduce la entrada a actualizar")
        titulo = input("Introduce el titulo de la web:")
        descripcion = input("Introduce la descripción de la web:")
        url = input("Introduce la url de la web:")
        categoria = input("Introduce la categoría de la web:")
        # abro el archivo original
        archivo = open("datos.txt",'r')
        contenidoinicio = archivo.readlines()
        contenidofinal = []
        # busco linea a linea
        for fila in contenidoinicio:
            if criterio.lower() in fila.lower():
                s = ","
                nl = "\n"
                contenidofinal.append(titulo+s+descripcion+s+url+s+categoria+nl)
            else:
                contenidofinal.append(fila) #lo agrego
        archivo.close()
        # abro el archivo pero en modo w
        archivo = open("datos.txt",'w')
        #repaso el contenido final
        for fila in contenidofinal:
            archivo.write(fila) #escribo en el archivo
        archivo.close() # cierro el archivo
    elif opcion == "5":
        print("Eliminamos un registro")
        criterio = input("Introduce la entrada a eliminar")
        # abro el archivo original
        archivo = open("datos.txt",'r')
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
        archivo = open("datos.txt",'w')
        #repaso el contenido final
        for fila in contenidofinal:
            archivo.write(fila) #escribo en el archivo
        archivo.close() # cierro el archivo
    elif opcion == "6":
        print("Salimos")
        sys.exit()
    menu()

menu()
