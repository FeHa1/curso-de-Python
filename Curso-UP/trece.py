# Se quiere armar una fiesta de cumpleaños, para lo que se necesita saber
# si los invitados son vegetarianos, veganos o normales
# se pide ingresar invitados hasta que se ingrese un cero
# Generar una funcion que retorne el porcentaje de vegetarianos sobre el total de invitados.

# v - vegetariano
# X - vegano
# N - normal

vegetariano = 0
vegano = 0
normal = 0
invitados = input("Ingrese V - vegetariano, X - vegano, N - normal, 0 - para salir: ")

def fiesta(vegetariano, vegano, normal): 
    
    invitados = input("Ingrese V - vegetariano, X - vegano, N - normal, 0 - para salir: ")

    while != "0":
        if invitados == "V":
            invitados = vegetariano + 1 # seria lo mismo poner vegetariano += 1
        if invitados == "X":
            invitados = vegano + 1 
        if invitados == "N":
            invitados = normal + 1
        
        
        invitados = input("Ingrese V - vegetariano, X - vegano, N - normal, 0 - para salir: ")
    
    total = vegetariano + vegano + normal
    porcentaje = (vegetariano*100)/total
    return porcentaje

print(fiesta(vegetariano, vegano, normal))



### OTRO EJERCICIO

# Se registran las ventas de una floreria de forma semanal
# considerando 3 productos: ramo de rosas, jazmines y camelias
# Se pide:
# Una funcion que calcule el total semanal de cada producto
# Una funcion que retorne el porcentaje de rosas sobre el total 
# Una funcion que retorne el maximo vendido en la semana por producto

rosas = []
jazmines = []
camelias = []

for indice in range(7): # el range es para generar un rango de numero, y el parametro es 7 porque nos pide las ventas en una semana

    tipo = input("Ingrese producto R, J, C")
    cant = int(input("Ingrese la cantidad: "))

    if(tipo == "R"):
        rosas.append(cant)
    if(tipo == "J"):
        jazmines.append(cant)
    if (tipo == "C"):
        camelias.append(cant)

# La funcion recibe un arreglo de productos

def total_semanal(producto):

    total = 0
    for p in producto:
        total += p

    return total

def calcular_maximo(producto):

    total = 0 
    for p in producto: 
        if p > max: 
            max = p

    return max 

total_semanal(rosas)
total_semanal(jazmines)
total_semanal(camelias)