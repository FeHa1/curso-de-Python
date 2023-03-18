# Ingrese numeros hasta que el usuario ingrese 0. Calcular y mostrar: 
# a) La cantidad de numeros positivos pares multiplos de 5. 
# b) La cantidad de numeros primos. 
# c) El promedio de aquellos numeros impares multiplos de 3. 

num = int(input("Ingrese numeros hasta que ingrese 0: "))
Cant = 1
NumerosPares = 0
NumerosPrimos = 0
NumerosImpares = 0


while num != 0: 
    
    cont = 0 # lo dejo adentr del 'while' para que se reinicie cada vez que entra un valor nuevo, y no se acumule. 

    if (num % 2 == 0) and (num % 5 == 0):
        NumerosPares += 1  # contador 

    if (num % 2 != 0) and (num % 3 == 0): 
        NumerosImpares += num # aca es un acumulador porque tenemos que irlo sumando para despues sacar el promedio 
        Cant += 1

    #if num > 1:
    for i in range(1, num):
        if num % i == 0:
            cont += 1
        
    if cont == 1:
        NumerosPrimos += 1



    num = int(input("Ingrese numeros hasta que ingrese 0: "))
    

promedio = NumerosImpares/Cant # aca tene que dividirlo por la cantidad de numerosimpares

print(promedio)
print(NumerosPares)
print(NumerosPrimos) 
print(cont)