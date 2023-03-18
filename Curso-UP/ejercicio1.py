### PRIMER PARCIAL:

## EJERCICIO 1) 
# Realizar funciones (siempre que dice funcion es que debe estar dentro de un "def") que cumplan las 
# siguientes tareas: 

# a. Debe leer un numero de teclado y devolverlo siempre y cuando sea múltiplo del recibido por parámetro, 
# caso contrario debe volver a pedirlo.

# b. Recibe 3 argumentos y retorna el mayor de ellos.

# c. Debe leer 3 números y con el mayor de ellos leer otro número que sea múltiplo de ese número y devolverlo.


# a.

n = int(input("Ingrese un numero: "))


def mult(n): 
    
    n2 = int(input("Ingrese otro numero: "))
    m = False # esto lo hago para que obligarlo a que ingrese al bucle. 

    while m == False:
        if n2 % n == 0:
            m = True
            print("n2 es multiplo del numero ingresado: ")
        else: 
            print("Ingrese otro numero que sirva: ")
            n2 = int(input("Ingrese otro numero: ")) 


mult(n)           

# b.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
m = 0

def mayor(num1, num2, num3, m):

    if num1 > num2:
        if num1 > num3: 
            m = num1
        else: 
            m = num3

    elif num2 > num3:
        m = num2
    else: 
        m = num3 

    return m

print(mayor(num1, num2, num3, m))

# c.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
m = 0

def mayor(num1, num2, num3, m):

    if num1 > num2:
        if num1 > num3: 
            m = num1
        else: 
            m = num3

    elif num2 > num3:
        m = num2
    else: 
        m = num3 

    return m

print(mayor(num1, num2, num3, m))


def mult(m):

    n = int(input("ingrese otro numero multiplo del mas grande: "))
    q = False # lo hago paa que directamente entreen el bucle

    while q == False: 
        if m % n == 0: 
            q = True
            print("El numero ingresado si es multiplo")
        else:
            print("Ingrese otro numero que funcione")
            n = int(input("ingrese otro numero multiplo del mas grande: "))

print(mult(m))
