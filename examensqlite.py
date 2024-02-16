import sqlite3
import sys

def menu():
    print("Escoge una opción:")
    print("1.-Lista libros")
    print("2.-Buscar libros")
    print("3.-Insertar libro")
    print("4.-Actualizar libro")
    print("5.-Eliminar libro")
    print("6.-Salir")
    opcion = input("Escoge una opción: ")
    if opcion == "1":
        print("Listado de registros")
        conexion = sqlite3.connect("libros.db")
        cursor = conexion.cursor()
        peticion = "SELECT * FROM libros"
        cursor.execute(peticion)
        while True:
            fila = cursor.fetchone()
            if fila is None:
                break
            print(fila)
        conexion.commit()
        conexion.close()
    elif opcion == "2":
        print("Buscamos un libro")
        titulo = input("Introduce el titulo del libro:")
        conexion = sqlite3.connect("libros.db")
        cursor = conexion.cursor()
        peticion = "SELECT * FROM libros WHERE titulo LIKE '%"+titulo+"%'"
        while True:
            fila = cursor.fetchone()
            #if fila is None:
            #    break
            print(fila)
        conexion.commit()
        conexion.close()
    elif opcion == "3":
        print("Insertamos un libro")
        titulo = input("Introduce el titulo: ")
        autor = input("Introduce el autor: ")
        anio = input("Introduce el año: ")
        conexion = sqlite3.connect("libros.db")
        cursor = conexion.cursor()
        peticion = "INSERT INTO libros VALUES (NULL,'"+titulo+"','"+autor+"','"+str(anio)+"')"
        cursor.execute(peticion)
        conexion.commit()
        conexion.close()
        print("Tu registro se ha insertado correctamente")
    elif opcion == "4":
        print("Actualizamos un libro")
        print("Insertamos un libro")
        identificador = input("Introduce el identificador: ")
        titulo = input("Introduce el titulo: ")
        autor = input("Introduce el autor: ")
        anio = input("Introduce el añi: ")
        conexion = sqlite3.connect("libros.db")
        cursor = conexion.cursor()
        peticion = "UPDATE libros SET titulo = '"+titulo+"',autor='"+autor+"',anio='"+anio+"' WHERE Identificador="+identificador+""
        cursor.execute(peticion)
        conexion.commit()
        conexion.close()
        print("Tu registro se ha insertado correctamente")
    elif opcion == "5":
        print("Eliminamos un registro")
        identificador = input("Introduce el id del registro a eliminar: ")
        conexion = sqlite3.connect("discos.db")
        cursor = conexion.cursor()
        peticion = "DELETE FROM libros WHERE Identificador = "+identificador+""
        cursor.execute(peticion)
        conexion.commit()
        conexion.close()
    elif opcion == "6":
        print("Salimos")
        sys.exit()
    menu()

menu()
