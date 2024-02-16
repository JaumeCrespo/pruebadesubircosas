import sys
import os


modelo = {
    'productos':['nombre','descripcion','precio','peso','medidas'],
    'clientes':['nombre','email','telefono'],
    'fechas':['fecha','pedido']
}

def introduccion():
    print("╔══════════════════════════╗")
    print("║ Programa de empresa v.01 ║")
    print("║  Jose Vicente Carratalá  ║")
    print("╚══════════════════════════╝")
    input("Pulsa una tecla para continuar...")
    menuprincipal()

def limpiaPantalla():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def menuprincipal():
    limpiaPantalla()
    print("Menú principal")
    print(":::::::::::::::::::::::")
    print("Escoge un mantenimiento:")
    print("╔══╦═════════════════")
    for indice,opcion in enumerate(modelo):
        print("║"+str(indice)+" ║"+opcion)
    print("╚══╩═════════════════")
    opcion = input("Escoge una opcion: ")
    indice = int(opcion)
    categoria = list(modelo.keys())[indice]
    menu(modelo[categoria],categoria)    

def menu(modelodedatos,opcionseleccionada):
    limpiaPantalla()
    print("Menú "+opcionseleccionada)
    print("::::::::::::::::::::")
    print("Escoge una opcion: ")
    print("1.-Listar registros")
    print("2.-Buscar registros")
    print("3.-Insertar registros")
    print("4.-Actualizar registros")
    print("5.-Eliminar registros")
    print("6.-Menú principal")
    print("7.-Salir")
    opcion = input("Opción escogida: ")
    if opcion == "1":
        print("Listamos registros")
        archivo = open(opcionseleccionada+".txt",'r')
        for linea in archivo:
            print(linea)
        archivo.close()
    elif opcion == "2":
        print("Buscamos registros")
        termino = input("Introduce el termino que buscar: ")
        archivo = open(opcionseleccionada+".txt",'r')
        for linea in archivo:
            if termino in linea:
                print(linea)
        archivo.close()
    elif opcion == "3":
        print("Insertamos registros")
        cadena = ""
        for entidad in modelodedatos:
            cadena += input("Introduce "+entidad+": ")+","
        cadena += "\n"
        print("Guardamos")
        archivo = open(opcionseleccionada+".txt",'a')
        archivo.write(cadena)
        archivo.close()
    elif opcion == "4":
        print("Actualizamos registros")
        termino = input("Introduce el termino que actualizar: ")
        archivo = open(opcionseleccionada+".txt",'r')
        contenido = ""
        for linea in archivo:
            if not termino in linea:
                contenido += linea
            else:
                for entidad in modelodedatos:
                    contenido += input("Introduce "+entidad+": ")+","
                contenido += "\n"
        archivo.close()
        archivo = open(opcionseleccionada+".txt",'w')
        archivo.write(contenido)
        archivo.close()
    elif opcion == "5":
        print("Eliminamos registros")
        termino = input("Introduce el termino que eliminar: ")
        archivo = open(opcionseleccionada+".txt",'r')
        contenido = ""
        for linea in archivo:
            if not termino in linea:
                contenido += linea
        archivo.close()
        archivo = open(opcionseleccionada+".txt",'w')
        archivo.write(contenido)
        archivo.close()
    elif opcion == "6":
        print("Menú principal")
        menuprincipal()
    elif opcion == "7":
        print("Salimos")
        sys.exit()
    input("Pulsa una tecla para continuar..."   )
    menu(modelodedatos,opcionseleccionada)

introduccion()
