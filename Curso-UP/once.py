# # Calcuar el promedio de 10 numeros 

# x = 10  # declaro una variable

# valores = [5, 7, 11, 9, 8, 1, 0, 14, 78, 13] # declaro un arreglo con 10 numeros
# # indice 0 al 9 (en este caso porque hay 10 numeros pero el ejecutor empieza a contar desde el 0 que es el "5" en este caso)

# print(valores[1]) # muestra el 7 

# indice = 0
# print(valores[indice])

# suma = 0
# while indice < 10:
#     print(valores[indice])
#     suma += valores[indice]
#     indice = indice + 1 

# promedio = suma/indice



# Buscar y mostrar el valor maximo del arreglo 
valores = [5, 7, 11, 9, 8, 1, 0, 14, 78, 13]

n = len(valores) # El largo del arreglo

print(n)


#Buscar y mostrar el valor maximo del arreglo
valores = [5, 7, 11, 9, 8, 1, 0, 14, 78, 13] 

maximo = valores[0]

for v in valores: # la "v" es para que recorra los valores de la lista
    if v > maximo: 
        maximo = v
print(maximo)

#TABLA DE VALORES DE AYUDA PARA ENTENDER
maximo  v   vuelta
    5   5       1 # el maximo es 5 porque le habiamos asignado la variable "maximo = valores[0]" 
    5   7       2
    7   11      3    

# Cargar por teclado un aarreglo de 5 elementos. 

valores = []
cont = 0

while cont <5:
    valores.append(int(input("Ingrese un valor: ")))
    cont += 1

print(valores)  

