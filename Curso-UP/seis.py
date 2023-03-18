# Pedir el ingreso de valores por consola hasta que se detecte un -1 y calcular el promedio de los valores
# ingresados.

# != (not equal)
# ! (not)

x = int(input("Ingrese un numero: "))
suma = 0
cont = 0

while x != -1:
    suma = suma + x 
    cont = cont + 1
    x = int(input("Ingrese un numero: "))
prom = suma/cont # el termino ¨/¨ es para dividir.
print("El promedio es: " + str(prom)) # el ¨str¨ es para transformar el valor a string

