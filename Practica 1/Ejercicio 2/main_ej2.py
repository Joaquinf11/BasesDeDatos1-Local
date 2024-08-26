import ejercicio2

def mostrarMenu():
    print("ABM de Archivo de Metadata\n")
    print("0 - Salir\n" +
          "1 - Mostrar archivo\n" +
          "2 - Alta\n" + 
          "3 - Modificacion\n" +
          "4 - Baja\n" +
          "5 - Iniciar archivo\n")

mostrarMenu()
accion= input("Ingrese una opcion: ")

while(accion.upper != '0'):
    if accion.upper == '1':
        ejercicio2.mostrarArchivo()
    elif accion.upper() == '2':
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        codigo =input("Ingrese codigo: ")
        ejercicio2.insert(apellido,nombre,codigo)
        print("Cliente agregado con exito.")
    elif accion.upper() == '3':
        old_codigo= input("Ingrese el codigo del cliente que desea modificar: ")
        new_nombre=input("Ingrese el nombre: ")
        new_apellido=input("Ingrese el apellido: ")
        new_codigo =input("Ingrese codigo: ")
        ejercicio2.update(old_codigo,new_apellido,new_nombre,new_codigo)
        print("Cliente modificado con exito.")
    elif accion.upper() == '4':
        codigo=input('Ingrese el codigo del cliente que desea eliminar: ')
        ejercicio2.delete(codigo)
        print("Cliente eliminado con exito.")
    elif accion.upper() == '5':
        ejercicio2.inicarArchivo()
        print("Archivo generado con exito.")
    mostrarMenu()
    accion= input("Ingrese una opcion: ")

