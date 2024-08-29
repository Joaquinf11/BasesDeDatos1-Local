import ejercicio3

def mostrarMenu():
    print("ABM de Archivo de Metadata\n")
    print("0- Salir\n" +
          "1 - Generar archivo nuevo \n" +
          "2 - Mostrar archivo\n" +
          "3 - Alta\n" + 
          "4 - Modificacion\n" +
          "5 - Baja\n" + 
          "6 - Compactar \n"
          )

def main():
    mostrarMenu()
    accion= input("Ingrese una opcion: ")

    while(accion != '0'):
        if accion == '1':
            try:
                ejercicio3.generarArchivo()
                print("Archivo generado exitosamente.")
            except Exception as e:
                print(f"Error al generar archivo: {e}")
        elif accion == '2':
            try:
                ejercicio3.mostrarArchivo()
            except Exception as e:
                print(f"Error al mostrar archivo: {e}")
        elif accion == '3':
            try:
                print("Ingrese los datos")
                datos= ejercicio3.ingresarDatos()
                ejercicio3.insert(None, datos)
                print("Alta generada exitosamente.")
            except Exception as e:
                print(f"Error al dar de alta: {e}")
        elif accion == '4':
            try:
                index=input("Ingrese el indice que desea modificar: ")
                print("Ingrese los datos")
                datos= ejercicio3.ingresarDatos()
                ejercicio3.update(index, datos)
                print("Modificacion generada exitosamente.")
            except Exception as e:
                print(f"Error al realizar modificacion: {e}")
        elif accion == '5':
            try:
                index=input("Ingrese el indice que desea eliminar: ")
                ejercicio3.delete(index)
                print("Registro eliminado exitosamente.")
            except Exception as e:
                print(f"Error al dar de baja: {e}")
        
        mostrarMenu()
        accion=input("Ingrese una opcion:")

main()