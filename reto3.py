 
num = int(input("Ingresa un número para obtener su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

