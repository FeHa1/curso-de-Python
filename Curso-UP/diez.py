# Crear una funcion que reciba como parametro el numero entero y retorne el factor de ese numero
# Ayuda: factorial de 5 es 120 5x4x3x2x1

# def calcular_factorial(num):
#     factorial - 1 # neutro de multiplicacion
#     while num > 0: # tambien se podia poner !=0 (!= significa distinto)
#         factorial = factorial*num
#         num = num - 1 # actualizo la variable de control
#     return factorial

# numero = int(input("Ingrese un numero: "))

# resultado = calcular_factorial(numero)

# print("El resultado es: "+str(resultado))

# factorial       num
#     1       x    5
#     5       x    4
#     20      x    3
#     60      x    2  


# Laura hace la fiesta de cumpleaños de su hijo y quiere contar cuantos nenes y cuantas nenas van para comprar mascaras
# Va a contar hasta ingresar un 0
# Si ingresa F es una nena, si ingresa M se suma un nene
# Sacar el porcentaje de nenas de la fiesta

def fiesta():

    cant_nenes = 0
    cant_nenas = 0

    invitado = input("Ingrese F - para nenas, M - para nenes o 0 para salir: ")

    while invitado != "0": # porque como estamos trabajando sin valores numericos en el input ese 0 va a entrar como cadena de caracteres
    
        if invitado == "F": 
            cant_nenas = cant_nenas + 1
        else:
            cant_nenes = cant_nenes + 1 

        invitado = input("Ingrese F - para nenas, M - para nenes o 0 para salir: ") # si no le ponemos esto nunca saldria del ¨while¨ ni se actualizarian los datos. 

    total = cant_nenas + cant_nenes
    porcentaje = (cant_nenas*100)/total

    print("La cantidad de nenas es ", cant_nenas)
    print("La cantidad de nenes es ", cant_nenes)

    return porcentaje # el ¨return¨ queda solo porque no tengo que retornar ninguna variable, y porque ya usamos el ¨print()¨ para mostrar la cantidad

# Codigo principal
porcentaje_invitadas = calcular_invitados()

print("El porcentaje de nenas es: ",porcentaje_invitadas)






