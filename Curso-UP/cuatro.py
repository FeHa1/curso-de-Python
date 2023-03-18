# Decir si un numero es mayor, mmenor o igual a 0
# Mostrar un mensaje en cada caso

num = int(input("Coloque un numero: "))

if num <0:
    print("Este numero es menor que 0")
elif num >0: # se usa cuando tengo una condicion 
    print("Este numero es mayor que 0")
else: # toma todo lo que no cumplen las conficiones previas, solo se puede usar una vez a diferencia de "if" o "elif"
    print("Este numero es igual que 0")

 