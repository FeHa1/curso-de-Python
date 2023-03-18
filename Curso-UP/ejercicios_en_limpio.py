# 1) Realizar un programa que solicite el ingreso de 3 números y mostrar el mayor de ellos.

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))

if a > b:
    if a > c:
        print(a)
    else: 
        print(c)

elif b > c:
    print(b)
else:
    print(c)

# 2) Solicitar el ingreso de números mientras la suma de ellos no supere los 500. 
#    Al final mostrar la suma de los múltiplos de 3.

num = int(input("Ingrese numeros: "))
lista = 0
cont = 1
MultiploDe3 = 0

while lista < 500:  
    lista = lista + num # acumulador: estoy acumulando valores (es como una alcancia)
    if num % 3 == 0: 
        MultiploDe3 += num

    num = int(input("Ingrese numeros: "))
    cont += 1 # contador: porque va de a 1 

print(cont)
print(lista)
print(MultiploDe3)
   


# Calcula el sueldo de una persona, conociendo la cantidad de horas que trabaja en el mes y el valor de la hora.

cant_hora = 240 
valor_hora = 3000
sueldo = cant_hora*valor_hora
print(sueldo)



# Se quiere calcular el precio total que se va a pagar por un producto utilizando una función que reciba por
# parámetro el precio del producto. Teniendo en cuenta las siguientes opciones:

# Si se paga en efectivo 10% de descuento
# Si se paga con tarjeta de débito 5% de descuento
# Si se paga con tarjeta de crédito un recargo del 15%

# Se pide luego, mostrar por pantalla el importe total a pagar según el medio de pago elegido.

def calcular_precio(): 
    remera = 250 
    efectivo = 0
    tarjeta_debito = 0
    tarjeta_credito = 0

    valores = input("Ingrese E - para efctivo, D - para tarjeta de debito y C - para tarjeta de credito: ") 

    if valores == "E": 
        efectivo += (remera*10)/100
        print(efectivo)
    if valores == "D":
        tarjeta_debito += (remera*5)/100
        print(tarjeta_debito)
    if valores == "C": 
        tarjeta_credito += (remera*15)/100
        print(tarjeta_credito)
    
    #return

print(calcular_precio())



# ### TRABAJO 2-B
# # Ingresas 10 números, los suma y los divide por 10 (cantidad de números ingresados) y el resultado es 
# # el promedio. 

# valores = []
# cont = 0

# while cont < 10:
#       valores.append(int(input("Ingrese un valor: ")))
#       cont += 1  
      
# def promedio(valores):
#       total = valores[0]
#       for v in valores:
#             if v < total:
#                   total = v
#       return total

# prome_fun = total/10

# print(promedio(valores))



### TRABAJO 3-B
# Dado el siguiente array:
# numeros = [15, 74,110,9,8,1,0,14,78,13,150,4]
# Mostrar la suma de todos los elementos pares contenidos en el arreglo.

# numeros = [15, 74,110,9,8,1,0,14,78,13,150,4]

# def sumar_pares(numeros):
#       suma = 0 
      
#       for v in numeros:
#          if v%2 == 0: 
#             suma += v
            
#       return suma

# print(sumar_pares(numeros))




### TRABAJO 4-B   

# Cargar un array con 5 números aleatorios.
# Generar una función que reciba como parámetros el array y dos números enteros y retorne la suma de los valores 
# que se correspondan a esas posiciones del array.

# valores = []
# cont = 0

# while cont < 5:
      
#       valores.append(int(input("Ingrese un numero: ")))
#       cont += 1


# def suma(valores):
      
#       dato1 = int(input("Ingrese el primer numero entero: ")) 
#       dato2 = int(input("Ingrese un segundo numero entero: "))
#       suma_datos = (valores[dato1]) + (valores[dato2])

#       return suma_datos

# print(suma(valores))



### EVALUACION
# Realizar un programa para una empresa, el mismo debe registrar en las facturacion por dia. Dicho arreglo 
# tiene la capacidad para un mes completo (30 dias)
# se pide:
# Cargar todo arreglo con los importes de facturacion diario.
# Determinar el dia que hubo mayor facturacion
# El promedio de facturacion.

# valores = []
# cant = 0 

# for indice in range(30): 

#       valores.append(int(input("Ingrese los recaudado en cada dia: ")))
#       cant += 1

# def calcular_maximo(producto):
#       total = 0
#       for p in producto:
#             if p > max: 
#                   max = p
      
      
#       return max

# total = cant/30     
# print(calcular_maximo) 



### TRABAJO 5-B
# Cargar un arreglo que contenga 10 números enteros.
# Generar una función que reciba como parámetro un número entero y lo busque dentro del arreglo. 
# La función deberá devolver la posición (indice) donde ubicó el valor y si no lo encuentra devolver -1. 

# valores = []
# cont = 0

# while cont < 10:
#       valores.append(int(input("Ingrese 10 numeros enteros: ")))
#       cont += 1

# def parametros():
#       valores.index(int(input("Ingrese uno de los numeros colocados anteriormente: ")))

# print(parametros)   


### TRABAJO 6-B
# Realizar la prueba de escritorio correspondiente utilizando los siguientes valores dentro del arreglo tiempos 
# [11.5, 8.8, 9.2, 4.7, 12.3, 6.9] 
# Validar si el código cumple correctamente con el requerimiento
# Realizar cambios o mejoras que considere necesario.


# # Tambla de valores:
# [11.5, 8.8, 9.2, 4.7, 12.3, 6.9]

# min     v       mejores
# 11.5    11.5    
# 11.5    8.8     8.8
# 8.8     9.2     
# 8.8     4.7     4.7
# 4.7     12.3    
# 4.7     6.9     



### TRABAJO 7-B
# El cumpleaños de Jaime, se desea armar la fiesta de cumpleaños de un niño de 6 años y se deben comprar máscaras, 
# por lo que se debe almacenar y procesar la siguiente información:
# - Se pueden ingresar hasta 10 niños y se dejará de introducir información si se ingresa -1
# - Se podrá elegir la máscara de Batman (B), Thor (T), La mujer maravilla (W).

# Se pide:
# - Mostrar la máscara más elegida y la cantidad de veces que se eligió
# - Mostrar el porcentaje de máscaras elegidas de Thor sobre el total de máscaras.


# def fiesta(amigos):
    
#     mascara_batman = 0
#     mascara_thor = 0
#     mascara_mujer_maravilla = 0

#     niños = input("Ingrese B - para Batman, T - para Thor, M - para Mujer Maravilla o -1 para salir: ")

#     while niños > 10 or niños != -1:
#         if niños == "B":
#             mascara_batman += 1
#         if niños == "T":
#             mascara_thor += 1
#         if niños == "M":
#             mascara_mujer_maravilla += 1

#         niños = input("Ingrese B - para Batman, T - para Thor, M - para Mujer Maravilla o -1 para salir: ")

#     total = mascara_batman + mascara_thor + mascara_mujer_maravilla
#     porcentaje_Thor = (mascara_thor*100)/total

#     return    

# print("El porcentaje de las mascaras de Thor vendidas fue de: ",porcentaje_Thor)


# def fiesta2(mascara_elegida):

#     total = 0
#     for v in mascara_elegida:
#         if v > max:
#             max = v
    
#     return max



### PRIMER PARCIAL:

## EJERCICIO 1) 
# Realizar funciones (siempre que dice funcion es que debe estar dentro de un "def") que cumplan las siguientes tareas, y además mostrar su uso mediante un ejemplo:

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




## EJERCICIO 2)
# Se necesita un sistema para realizar un censo poblacional casa por casa, por cada hogar se preguntan cuantas personas 
# viven en ella, y luego cuáles son sus edades, a lo que el sistema debe mostrar el promedio de edad. Al finalizar la 
# recorrida el sistema debe mostrar cuántos menores a 18 años se censaron y cuál es el promedio de edad de la familia 
# más longeva (El mayor promedio de edades).
# (Puede realizarse sin funciones). Se finaliza la carga cuando la cantidad de personas es 0 o menos.

# Ejemplo: 
# Cuantas personas viven: 2
# Edad: 40
# Edad: 30
# Promedio de edad: 35

# Cuantas personas viven: 3
# Edad: 42
# Edad: 50
# Edad: 17
# Promedio de edad: 36.3

# Cuantas personas viven: 0
# Menores censados: 1
# Familia mas longeva: 36.3


prom_longevo = 0
primer_numero = True
cont = 0
casas = "si"
menores = 0 # lo pongo afuera porque a este SI necesito irlo sumando para todas las casas, a diferencia del 'edades'

while casas == "si": 

    edades = 0 # lo pongo aca adentro para que los numeros que ingrese no se vayan sumando todos juntos, es para que se resete la suma
    num_personas = int(input("Ingrese la cantidad de personas de la casa: "))

    for i in range(0, num_personas):
        num_edad = int(input("Ingrese las edades: "))
        edades += num_edad # acumulador de las edades
        
        if edades < 18: 
            menores += 1 # contador de los menores de edad

    promedio = edades/num_personas
    print(promedio) 

    if primer_numero == True: 
        prom_longevo = promedio 
        primer_numero = False
    elif prom_longevo < promedio: 
        prom_longevo = promedio

    casas = str(input("¿Hay mas casas? si/no: "))   

print(menores)
print(prom_longevo)
    



### PRACTICA PARA RECUPERATORIO =

# Se quieren calcular las ventas semanales de un kiosco, se pide:

# Cargar un arreglo de 7 días con valores float que representen las ventas del día
# Calcular el promedio de ventas de la semana
# Calcular y mostrar el día que menos vendió. (Se pide el día no el valor)

# valores = []
# cont = 0 
# indice = 0

# while cont < 7: 
#     valores.append(float(input("Ingrese lo recaudado en cada dia: ")))
#     cont += 1

# def menores(valores): 
#     numeros = valores[0]
#     pos_min = 0

#     minimo = valores[0]
#     for v in range(len(valores)): 
#         if valores[v] < minimo:
#             minimo = valores[v] 
#             pos_min = v
    
#     return pos_min

# print(menores(valores)) 

# suma = 0

# def promedio(valores):
#     suma = 0
#     while cont < 7:
#         suma += valores[cont]
#     promedio = suma/cont    
    

#     return promedio

# print(promedio(valores))




### RECUPERATORIO = 

# # 1) 
# # En una florería se venden rosas y jazmines, las primeras valen $150 el ramo y las segundas $100. 
# # Se quiere calcular la venta semanal. Se pide:

# # *El total semanal en monto vendido. (Considerar ambos productos).
# # *El producto más vendido en la semana.
# # *La cantidad de rosas vendidas en un día dado

# rosas = 150
# jazmines = 100 
# ventas1 = []
# ventas2 = []

# for indice in range(7): 

#     tipo = input("Ingrese R para rosas y J para jarmines: ")
    
#     if (tipo == "R"):
#         ventas1.append(rosas)   
#     if (tipo == "J"): 
#         ventas2.append(jazmines)

# ventas_totales = (ventas1 + ventas2)


# def total_semanal(ventas_totales): 
    
#     ventas_totales = (ventas1 + ventas2)
#     total = 0
    
#     for p in ventas_totales:
#         total += p
    
#     return total

# print(total_semanal(ventas_totales))



# def cant_rosas(ventas1): 
    
#     max_rosas = 0
#     total = 0

#     for p in ventas1:
#         if p > max_rosas:
#             max_rosas = p

#     return max_rosas

# print(cant_rosas(ventas_totales))


# print(total_semanal(rosas))
# print(total_semanal(jazmines))




# # 2) 
# # Dado el siguiente arreglo de números arreglo = [12,49,10,83,2,98,64,17], se pide:

# # a- Generar una función que reciba como argumento el arreglo y retorne la suma de los valores en las posiciones pares.
# # b- Generar una función que reciba como argumento y el arreglo y un valor numérico y retorne, la suma del valor del 
# #    arrego que corresponde con la posición parámetro y la siguiente posición. Tip: Si se pasa por parámetro 4, será la 
# #    suma del valor en la posición 4 y la posición 5. Validar que los valores pasados no superen el tamaño del arreglo.


# # a- 

# arreglo = [12,49,10,83,2,98,64,17]    
# cont = 0

# def datos(arreglo):
#     num_pares = 0
#     cont = 0
    
#     for v in range(len(arreglo)): 
#         if v % 2 == 0: 
#             num_pares += arreglo[v]

#     total = num_pares + arreglo[cont]

#     return total

# print(datos(arreglo))


# # b- 

# arreglo = [12, 49, 10, 83, 2, 98, 64, 17]
# indice = 0

# def funcion(indice):

#     if indice >= 0 and indice < len(arreglo)-1:
#         suma = arreglo[indice] + arreglo[indice+1]
#     return suma

# print(funcion(indice))



#### OTRO RECUPERATORIO MAS = 

## Pregunta 1
# Dado el siguiente arreglo de números, v = [10,4,8,13,56,4,2,0].

# a) Realizar una función que reciba como parámetro el arreglo "v" y un número, y busque este número dentro del arreglo y devuelva la cantidad de veces que se repita. Ayuda: si se ingresa 
# como parámetro un 4, deberá devolver 2, si no se encuentra el valor devolverá 0.

# b) Realizar una función que reciba como parámetro un número N y retorne un arreglo que contenga N elementos de valor N. Ayuda: Si se ingresa un 4 deberá retornar un arreglo tal: [4,4,4,4].

# a-

v = [10,4,8,13,56,4,2,0]

def numeros(v):
    datos = v[0]
    i = 0
    r = int(input("Ingrese un numero: "))
    
    for i in range(len(v)):
        if r == v:
            i = v
        else:
            print(0)
    
    return 

print(numeros(v))





# Pregunta 2
# Se desea realizar los cálculos de los tiempos de una carrera de caballos. Para ello se pide:

# *Ingresar los 10 mejores tiempos, los valores vienen en formato float.
# *Calcular el promedio de tiempos
# *Calcular el peor tiempo. (Máximo)

tiempos = float(input("Ingrese los tiempos de los corredores: "))
lista = []
cont = 0

while cont < 10:
    
    lista.append(tiempos)
    tiempos = float(input("Ingrese los tiempos de los corredores: "))
    

def promedio(lista):
    suma = 0
    while cont < 10:
        suma += lista[cont]
    promedio = suma/cont

    return promedio
print(promedio(valores))


maximo = lista[0]

for v in lista:
    if v > maximo:
        maximo = v
print(maximo)



### FINAL DE PROGRAMACION 1

# Se quiere generar una estadistica de las estaturas de los ni;os de un curso, para eso se pide
# Cargar alturas hasta que se ingrese 0. 
# Determinar el promedio de alturas al final de la carga.
# Determinar la cantidad de alturas mayores a 120 cm.

altura = int(input("Ingrese la altura de los niños hasta ingresar un '0': "))
cont1 = 0
cont2 = 0
acum = 0

while altura != 0: 
    altura = int(input("Ingrese la altura de los niños hasta ingresar un '0': "))
    cont1 += 1
    acum += altura
    altura = int(input("Ingrese la altura de los nuños hasta ingresar un '0': ")) # se repite aca para que el bucle no quede repitiendose de manera infinita. 

promedio = acum/cont1

for v in altura: 
    if v > 120:
        cont2 += 1 

print("El promedio de los numeros es: ", promedio)
print("Las alturas mayores a 120 cm son: ", cont2)


# Dado el siguiente arreglo de numeros, x = [2, 5, 6, 3, 9, 12], se pide generar una funcion que reciba por parametros el arreglo y un valor numerico y retorne True, en caso que el valor 
# agregado sea divisible por alguno de los valores del arreglo. 
# Importante: alcanza con que sea divisible por alguno de los valores del arreglo. Si no resulta divisible por ninguno devolve False. 

x = [2, 5, 6, 3, 9, 12]
f = int(input("Ingrese cualquier numero: "))

def num(x, f): # tengo que poner todo lo que voy a usar en los parametros de 'num()'
    for v in x: 
        if f % v == 0: 
            return True
        
    return False

print(num(x, f))



