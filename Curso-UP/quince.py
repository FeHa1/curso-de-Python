# Cargar un arreglo de numeros hasta que se ingrese -1.
# Generar una funcion que intercambie el primer y ultimo elemento del arreglo.
# Generar una funcion que intercambie dos posiciones del arreglo pasadas por parametro. 

valores = []
cont = 0

while cont != -1:
    valores.append(int(input("Ingrese los numeros que quiera, si coloca -1 se acaba el proceso: ")))
    cont += 1

def intercambiar(arreglo):

    aux = arreglo[0]
    arreglo[0] = arreglo[len(arreglo)-1] # se pone el "-1" asi nos da la ultima posicion, porque no sabemos cuantos n° va a poner el usuario asi que el ultimo valor se marca asi.
    arreglo[len(arreglo)-1] = aux

    return

def calcular(array, pos1, pos2): 
    if (pos1 >= 0 and pos1 < len(arreglo)) and (pos2 >= 0 and pos2 < len(arreglo)):
        aux = arreglo[poa1]
        arreglo[pos1] = arreglo[pos2]
        arreglo[pos2] = aux

    return arreglo

pos1 = int(input("Ingrese posision 1: "))
pos2 = int(input("Ingrese posision 2: "))



# Dado un arreglo de 10 numeros.
# Generar una funcion que retorne la posicion del valor maximo.

numeros = [5, 8, 4, 3, 8, 11, 55, 9, 45, 16]

def maximo(numeros):
    maximo = numeros[0]
    pos_max = 0
    
    for i in range(len(numeros)):  # el "range()" te da un rango de numeros, en este caso le pedimos que recorra la lista.
        if numeros[i] > maximo:
            maximo = numeros[i]
            pos_max = i
    
    return pos_max

max = maximo(numeros)
print(max)


def maximo2(numeros):
    maximo = numeros[0]
    pos_max = 0
    i = 0

    while i < len(numeros)  # aca se usa el "while" solo porque en el anterior usamos "for" y la profe queria que vieramos ambas posibilidades.
        if numeros[i] > maximo:
            maximo = numeros[i]
            pos_max = i
        i += 1
        
    return pos_max 

max2 = maximo2(numeros)
print(max2)