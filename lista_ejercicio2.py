baul = []

while True:
    print("Opciones disponibles:")
    print("1. Agregar un artículo al baúl")
    print("2. Listar artículos del baúl")
    print("3. Borrar el último elemento del baúl")
    print("4. Borrar un artículo del baúl")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        articulo = input("Ingrese el articulo a agregar: ")
        baul.append(articulo)
        print("Artículo agregado al baúl.")
    
    elif opcion == "2":
        print("Artículos del baúl:")
        for i, articulo in enumerate(baul):
            baul.sort()
            print(i, "-", articulo)
    
    elif opcion == "3":
        if len(baul) == 0:
            print("El baúl está vacío.")
        else:
            ultimo_articulo = baul.pop()
            print("Se ha borrado el artículo:", ultimo_articulo)
    
    elif opcion == "4":
        print("Artículos del baúl:")
        for i, articulo in enumerate(baul):
            print(i, "-", articulo)

        if len(baul) == 0:
            print("El baúl está vacío.")
        else:
            index_borrar = int(input("Ingrese el índice del artículo a borrar: "))
            if index_borrar < 0 or index_borrar >= len(baul):
                print("Índice inválido.")
            else:
                articulo_borrar = baul.pop(index_borrar)
                print("Se ha borrado el artículo:", articulo_borrar)
    
    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


