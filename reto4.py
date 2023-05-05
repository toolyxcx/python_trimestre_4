
num = int(input("Ingresa un número del 1 al 10 para obtener su tabla de multiplicar: "))

if num < 1 or num > 10:
    print("Error: El número debe estar entre 1 y 10.")
else:
    print(f"Tabla de multiplicar del {num} en orden inverso:")
    for i in range(10, 0, -1):
        print(f"{num} x {i} = {num * i}")


