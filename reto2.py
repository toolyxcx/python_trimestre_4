precio_pasaje = 2950
tipo_tarjeta = input("Ingrese el tipo de tarjeta (corriente o personalizada): ")
saldo_tarjeta = float(input("Ingrese el saldo de su tarjeta: "))

if tipo_tarjeta == "corriente":
    if saldo_tarjeta >= precio_pasaje:
        saldo_tarjeta = saldo_tarjeta - precio_pasaje
        print("Pago realizado. El saldo de su tarjeta es:", saldo_tarjeta)
    else:
        print("Saldo insuficiente. ¿Desea cargar su tarjeta? (si/no)")
        respuesta = input()
        if respuesta == "si":
            saldo_carga = float(
                input("Ingrese la cantidad de dinero que desea cargar en su tarjeta: "))
            saldo_tarjeta = saldo_tarjeta + saldo_carga
            if saldo_tarjeta >= precio_pasaje:
                saldo_tarjeta = saldo_tarjeta - precio_pasaje
                print("Pago realizado. El saldo de su tarjeta es:", saldo_tarjeta)
            else:
                print("Saldo insuficiente. El saldo de su tarjeta es de",
                      saldo_tarjeta)
        else:
            print("Pago no realizado. El saldo de su tarjeta es de", saldo_tarjeta)
elif tipo_tarjeta == "personalizada":
    if saldo_tarjeta < 0:
        print("Su tarjeta tiene una deuda pendiente de",
              abs(saldo_tarjeta), "pesos.")
        respuesta = input("¿Desea pagar su deuda? (si/no)")
        if respuesta == "si":
            saldo_carga = float(
                input("Ingrese la cantidad de dinero que desea cargar en su tarjeta: "))
            saldo_tarjeta = saldo_tarjeta + saldo_carga
            if saldo_tarjeta >= 0:
                saldo_prestado = precio_pasaje
                saldo_tarjeta = saldo_tarjeta - saldo_prestado
                print("Pago realizado con préstamo de", saldo_prestado,
                      "pesos. El saldo de su tarjeta es:", saldo_tarjeta)
            else:
                print("Saldo insuficiente. El saldo de su tarjeta es de",
                      saldo_tarjeta)
        else:
            print("Pago no realizado. El saldo de su tarjeta es de", saldo_tarjeta)

    else:
        if tipo_tarjeta == "personalizada":
            tiempo_transcurrido = float(
                input("Ingrese el tiempo transcurrido desde su último viaje (en minutos): "))

            if tiempo_transcurrido < 60 and saldo_tarjeta >= 0 and tiempo_transcurrido and tipo_tarjeta == "personalizada":
                print(
                    "Su último viaje fue hace menos de una hora. No se le cobrará nada.")
            else:
                saldo_prestado = max(0, precio_pasaje - saldo_tarjeta)
                saldo_tarjeta = saldo_tarjeta - saldo_prestado
                print("Pago realizado con préstamo de", saldo_prestado,
                      "pesos. ¿Desea cargar su tarjeta? (si/no)")
                respuesta = input()
                if respuesta == "si":
                    saldo_carga = float(
                        input("Ingrese la cantidad de dinero que desea cargar en su tarjeta: "))
                    saldo_tarjeta = saldo_tarjeta + saldo_carga
                    print("Pago realizado. El saldo de su tarjeta es:",
                          saldo_tarjeta)
                else:
                    print(
                        "Pago no realizado. El saldo de su tarjeta es de", saldo_tarjeta)
else:
    print("Tipo de tarjeta no reconocido. Por favor, ingrese 'corriente' o 'personalizada'.")
