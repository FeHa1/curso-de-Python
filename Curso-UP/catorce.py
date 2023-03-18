# Genenrar un podio, se pide:
# Cargar nombres de corredores hasta que se ingrese un -1 en un arreglo, cargar en otro arreglo los tiempos en 
# float (numeros reales) que hicieron en la carrera.
# Crear una funcion que reciba el arreglo de tiempos y genere un arreglo de 3 posiciones que contenga los mejores tiempos.

corredores = []
tiempo = []

nombre = input("Ingrese nombre de los corredores: ") # variable de control cuando esta fuera del "while"

while nombre != "-1":

    corredores.append(nombre)

    t = float(input("Ingrese el tiempo: "))
    tiempo.append(t)

    nombre = input("Ingrese nombre de los corredores: ")

def podio(tiempo):

    min = tiempo[0]
    mejores = [0]*3
    for i in range(3): # el "range()" te da un rango de numeros, del 0 hasta el numero que ponga entre parentesis.
        for v in tiempo:    
            if v < min and v != mejores[i]:
                min = v 

        mejores[i] = min
    
    return mejores


print(podio(tiempo))

# # Tambla de valores:
# [11.5, 8.8, 9.2, 4.7, 12.3, 6.9]

# min     v       mejores
# 11.5    11.5    
# 11.5    8.8     8.8
# 8.8     9.2     
# 8.8     4.7     4.7
# 4.7     12.3    
# 4.7     6.9     