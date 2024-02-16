
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="simulacro",
  password="simulacro",
  database="simulacro"
)

mycursor = mydb.cursor()




def menu():
    print("Selecciona una opción")
    print("1.-Listado de registros")
    print("2.-Introduce un nuevo registro")
    print("3.-Actualiza un registro")
    print("4.-Elimina un registro")
    seleccion = input("tu opción:")
    if seleccion == "1":
      mycursor.execute("SELECT * FROM discos")
      myresult = mycursor.fetchall()  
      for x in myresult:
        print(x)
    elif seleccion == "2":
      artista = input("Dime el artista")
      titulo = input("Dime el titulo")
      anio = input("Dime el año")
      mycursor.execute("INSERT INTO discos VALUES(NULL,'"+artista+"','"+titulo+"','"+anio+"')")
    menu()
menu()
