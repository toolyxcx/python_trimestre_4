instructores2557861 = {}

def agregar_modificar_instructor():
    nombre_instructor = input("Ingrese el nombre del Instructor: ")
    if nombre_instructor in instructores2557861:
        print("El instructor ya se encuentra registrado.")
        modificar = input("¿Qué desea modificar? (1. Nombre, 2. Materia, 3. Número, 4. Cancelar): ")
        if modificar == "1":
            nuevo_nombre = input("Ingrese el nuevo nombre del instructor: ")
            instructores2557861[nombre_instructor]['nombre'] = nuevo_nombre
            print("Nombre del instructor modificado correctamente.")
        elif modificar == "2":
            nueva_materia = input("Ingrese la nueva materia del instructor: ")
            instructores2557861[nombre_instructor]['materia'] = nueva_materia
            print("Materia modificada correctamente.")
        elif modificar == "3":
            nuevo_numero = input("Ingrese el nuevo número del instructor: ")
            instructores2557861[nombre_instructor]['numero'] = nuevo_numero
            print("Número modificado correctamente.")
        elif modificar == "4":
            print("Operación cancelada.")
        else:
            print("Opción inválida.")
    else:
        materia = input("Ingrese la materia del instructor: ")
        numero = input("Ingrese el número del instructor: ")
        instructores2557861[nombre_instructor] = {'materia': materia, 'numero': numero}
        print("El instructor se ha registrado correctamente.")

def buscar_instructor():
    texto_busqueda = input("Ingrese el instructor a buscar: ")
    encontrados = [nombre_instructor for nombre_instructor in instructores2557861.keys() if nombre_instructor.startswith(texto_busqueda)]
    if encontrados:
        print("Instructores encontrados:")
        for nombre_instructor in encontrados:
            print(nombre_instructor)
    else:
        print("No se encontraron instructores.")

def borrar_instructor():
    nombre_instructor = input("Ingrese el nombre del instructor a borrar: ")
    if nombre_instructor in instructores2557861:
        confirmacion = input("¿Está seguro de que desea borrar el instructor? (s/n): ")
        if confirmacion.lower() == "s":
            del instructores2557861[nombre_instructor]
            print("El instructor ha sido borrado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("El instructor no existe en el diccionario.")

def listar_instructores():
    if instructores2557861:
        print("Instructores disponibles:")
        for nombre_instructor, datos in instructores2557861.items():
            print(f"Nombre: {nombre_instructor}")
            print(f"Materia: {datos['materia']}")
            print(f"Número: {datos['numero']}")
            print()
    else:
        print("No hay instructores registrados.")

while True:
    print("\nOpciones disponibles:")
    print("1. Agregar/Modificar un instructor")
    print("2. Buscar un instructor")
    print("3. Borrar un instructor")
    print("4. Listar instructores")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agregar_modificar_instructor()
    elif opcion == 2:
        buscar_instructor()
    elif opcion == 3:
        borrar_instructor()
    elif opcion == 4:
        listar_instructores()
    elif opcion == 5:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
