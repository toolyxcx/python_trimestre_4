fruver = {}

while True:
    print("Fruver supermercados")
    print("1. Añadir/Modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        articulo = input("Ingrese el nombre del artículo: ")
        if articulo in fruver:
            print("El artículo ya se encuentra registrado.")
            print("Precio del artículo:", fruver[articulo]['precio'])
            modificar = input("¿Qué desea modificar? (1. Precio, 2. Tipo, 3. Cancelar): ")
            if modificar == "1":
                precio = int(input("Ingrese el nuevo precio del artículo: "))
                fruver[articulo]['precio'] = precio
                print("Precio del artículo modificado correctamente.")
            elif modificar == "2":
                tipo = input("Ingrese el nuevo tipo del artículo: ")
                fruver[articulo]['tipo'] = tipo
                print("Tipo del artículo modificado correctamente.")
            elif modificar == "3":
                print("Operación cancelada.")
            else:
                print("Opción inválida.")
        else:
            precio = int(input("Ingrese el precio del artículo: "))
            tipo = input("Ingrese el tipo del artículo: ")
            fruver[articulo] = {'precio': precio, 'tipo': tipo}
            print("El artículo se ha registrado correctamente.")

    elif opcion == 2:
        texto_busqueda = input("Ingrese el texto de búsqueda: ")
        encontradas = [articulo for articulo in fruver if articulo.startswith(texto_busqueda)]
        if encontradas:
            print("Artículos encontrados:")
            for articulo in encontradas:
                print(articulo)
        else:
            print("No se encontraron artículos.")

    elif opcion == 3:
        articulo = input("Ingrese el nombre del artículo a borrar: ")
        if articulo in fruver:
            confirmacion = input("¿Está seguro de que desea borrar el artículo? (s/n): ")
            if confirmacion.lower() == "s":
                del fruver[articulo]
                print("El artículo ha sido borrado correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print("El artículo no existe en el diccionario.")

    elif opcion == 4:
        if fruver:
            print("Artículos disponibles:")
            for articulo, datos in fruver.items():
                print(f"Artículo: {articulo}")
                print(f"Precio: {datos['precio']}")
                print(f"Tipo: {datos['tipo']}")
                print()
        else:
            print("No hay artículos registrados.")

    elif opcion == 5:
        print("Hasta luego.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
        
