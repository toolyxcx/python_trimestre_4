
import random

celular= input("Ingrese el número movil: ")

intentos = 3
while intentos > 0:
    clave = input("Ingrese su clave de 4 digitos: ")
    if len(clave) > 4 or len(clave) <4:
        print("¡Upps! Parece que tus datos de acceso no son correctos, Tienes tres intentos más.")
        intentos -= 1
    else:
        saldo_disponible = 4500
        print("su saldo es ",saldo_disponible)
        while True:
            opcion = input("Ingrese la opción que desea realizar (Sacar, Enviar, Recargar o Salir): ")
            
            if opcion == "sacar":
                tipo_retiro = input(" digite (si) para continuar el retiro en cajero ")
                if saldo_disponible < 2000:
                    print("No tienes suficiente saldo para hacer el retiro.")
                else:
                    cantidad_retiro = float(input("¿Cuánto dinero desea retirar? "))
                    if cantidad_retiro <= saldo_disponible:
                        saldo_disponible -= cantidad_retiro
                        codigo_retiro = str(random.randint(100000, 999999))
                        print(f"Se ha generado el código de retiro {codigo_retiro}.")
                    else:
                        print("No puedes retirar más dinero del que tienes en tu saldo.")
            
            elif opcion== "enviar":
                telefono_destino = input("Ingrese el número de teléfono al que desea enviar el dinero: ")
                cantidad_enviar = float(input("Ingrese la cantidad de dinero que desea enviar: "))
                if cantidad_enviar > saldo_disponible:
                    print("No tienes suficiente saldo para enviar esa cantidad de dinero.")
                else:
                    saldo_disponible -= cantidad_enviar
                    print(f"Se han enviado {cantidad_enviar} pesos al número de teléfono {telefono_destino}.")
            
            elif opcion == "recargar":
                cantidad_recarga = float(input("Ingrese la cantidad de dinero que desea recargar: "))
                confirmacion = input(f"Está seguro de que desea recargar {cantidad_recarga} pesos? (si/no) ")
                if confirmacion.lower() == "si":
                    saldo_disponible += cantidad_recarga
                    print(f"Se ha recargado {cantidad_recarga} pesos en tu cuenta. Nuevo saldo disponible: {saldo_disponible} pesos.")
                else:
                    print("Recarga cancelada.")
            
            elif opcion == "Salir":
                print("Gracias por usar Nequi.")
                break
            
        break
else:
    print("Ha excedido el número de intentos permitidos. espere 30 segundos.")

