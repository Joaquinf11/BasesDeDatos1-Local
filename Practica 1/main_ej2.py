import ejercicio2


       
print("El programa ha comenzado.") 
accion= input("Bienvenido seleccione una opcion: I(iniciar archivo) A(alta) | B(baja) | M(modificar) | S(salir): ")

while(accion.upper != 'S'):
    if accion.upper() == 'I':
        ejercicio2.crearArchivo()
        print("Se inicio el archivo correctamente.")
    if accion.upper() == 'A':
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        codigo =input("Ingrese codigo: ")
        ejercicio2.alta(apellido,nombre,codigo)
    elif accion.upper() == 'B':
        indice=int(input('Ingrese el cliente que desea eliminar: '))
        ejercicio2.baja(codigo)
    elif accion.upper() == 'M':
        indice=int(input('Ingrese el cliente que desea modificar: '))
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        codigo_modificar =input("Ingrese codigo: ")
        ejercicio2.modificar(codigo_modificar,apellido,nombre,codigo)
    else:
        print("Opción no válida.")
        break;
    accion= input("Bienvenido seleccione una opcion: A(alta) | B(baja) | M(modificar) | S(salir): ")

