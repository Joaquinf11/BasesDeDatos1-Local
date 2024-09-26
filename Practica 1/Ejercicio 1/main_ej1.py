import ejericio1
  
def mostrarMenu():
    print("ABM de Archivo de Metadata\n")
    print("0- Salir\n" +
          "1 - Mostrar archivo\n" +
          "2 - Alta\n" + 
          "3 - Modificacion\n" +
          "4 - Baja\n")

def main():
    print("0- Salir\n" +
        "1 - Generar archivo nuevo \n" +
        "2 - Manipular archivo existente\n")
    
    accion=input("Elija una opcion:"  )
    if accion == '0':
        return
    if accion == '1':
        nombre=input("Ingrese el nombre del archivo: ")
        ejericio1.generarArchivo(nombre)
        mostrarMenu()
    if accion == '2':
        nombre=input("Ingrese el nombre del archivo: ")
        ejericio1.nombreArchivo(nombre)
        mostrarMenu()
    accion= input("Ingrese una opcion: ")
    while(accion.upper != '0'):
        if accion == '1':
            ejericio1.mostrarArchivo()
        elif accion.upper() == '2':
            nombre=input("Ingrese el nombre: ")
            apellido=input("Ingrese el apellido: ")
            codigo =input("Ingrese codigo: ")
            ejericio1.insert(apellido,nombre,codigo)
        elif accion.upper() == '4':
            indice=int(input('Ingrese el indice que desea eliminar: '))
            ejericio1.delete(indice)
        elif accion.upper() == '3':
            indice=int(input('Ingrese el indice que desea modificar: '))
            nombre=input("Ingrese el nombre: ")
            apellido=input("Ingrese el apellido: ")
            codigo =input("Ingrese codigo: ")
            ejericio1.update(indice,apellido,nombre,codigo)
    
        else:
            print("Opción no válida.")
        mostrarMenu()
        accion= input("Ingrese una opcion: ")


if __name__ == '__main__':
    main()

