import ejericio1


       
def mostrarMenu():
    print("ABM de Archivo de Metadata\n")
    print("0- Salir\n" +
          "1 - Mostrar archivo\n" +
          "2 - Alta\n" + 
          "3 - Modificacion\n" +
          "4 - Baja\n")


while(accion.upper != '0'):
    if accion.upper() == '2':
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        codigo =input("Ingrese codigo: ")
        ejericio1.insert(apellido,nombre,codigo)
    elif accion.upper() == '4':
        indice=int(input('Ingrese el indice que desea eliminar: '))
        ejericio1.delete(indice)
    elif accion.upper() == '3':
        indice=int(input('Ingrese el indice que desea eliminar: '))
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        codigo =input("Ingrese codigo: ")
        ejericio1.update(indice,apellido,nombre,codigo)
    elif accion.upper == '1':
        ejericio1.mostrarArchivo()
    else:
        print("Opción no válida.")
        break;
    accion= input("Bienvenido seleccione una opcion: A(alta) | B(baja) | M(modificar) | S(salir): ")


