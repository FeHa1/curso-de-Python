# Ingresar dos numeros.
# Si uno es mayor que 25 y el otro es par calcular el promedio.
# en caso contrario sumarlos

num1 = input("Ingrese su primer numero: ")
num2 = input("Ingrese su segundo numero: ")

if num1 > 25 and num2%2==0:
    num3 = num1 + num2
    promedio = num3/2
    print("El promedio de los dos numeros es de "+promedio)
else:
    num3 = num1 + num2
    print("La suma de los dos numeros es de "+num3)


# Otra resolucion 

number_a = float(input("Insert the one number A: "))
number_b = float(input("Insert the one number B: "))
sumator = 0.0

if number_a >= 25 and number_b % 2 == 0.0:
    prom = (number_a + number_b)/2
    print("Case 0: "+ str(prom))
elif number_b >= 25 and number_a % 2 == 0.0: 
    prom = (number_a + number_b)/2
    print("Case 0: "+ str(prom))
else:
    sumator = number_a + number_b
    print("Return prom "+ str(sumator))

