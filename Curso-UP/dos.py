# Calcular el perimetro de un triangulo.
# Calcular el area de un cuadrado.

lado1 = input("Ingrese lado 1: ")
lado2 = input("Ingrese lado 2: ")
lado3 = input("Ingrese lado 3: ")

perimetro = int(lado1) + int(lado2) + int(lado3)

print("Este es el perimetro " + str(perimetro))

# Calculo del area del cuadrado

lado = int(input("Lado: "))
area = lado*lado

# Se usa ¨%s¨ para identificar que eso sea un String y ¨%d¨ para decir que es un digito.
# Esa es la manera en la que el ejecutor entiende que lo que esta entre parentesis lo tiene que presentar como un String y un numero.
print('%s %d' %("El area es: ",area)) # Esta es la forma vieja de hacerlo. 
