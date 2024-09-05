# 1. Solicitar la edad del cliente

edad = int(input("Ingresá la edad: ")) 

# 2. Verificar si la edad cumple con el requisito

puede = True if edad >= 18 else False  # Ternario

# 3. Indicar si el cliente puede o no entrar a la discoteca

if puede:
     print("podés entrar")
else:
     print("no podés entrar")
     