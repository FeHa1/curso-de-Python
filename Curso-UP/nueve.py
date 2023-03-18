# # Funciones

# # Declaracion 
# def saludar():
#     print("Hola mundo")

# # Invocacion
# saludar()

# # funcion con parentesis 
# def saludar(nombre)
#     print("Hola "+nombre)

# saludar(Fede)



# Dados tres numeros que corresponden con notas, calcular el promedio 
# Los valores deben ser mayores que 0 y menores o iguales a 10 

def promedio(nota1, nota2, nota3):
    prom = 0
    if (nota1 > 0 and nota1 <= 10) and (nota2 > 0 and nota2 <= 10) and (nota3 > 0 and nota3 <= 10):
        prom = (nota1 + nota2 + nota3)/3 # para sacar el promedio se divide por la cantidad de numeros
    return prom # 

nota1 = int(input("Nota de trimestre 1: "))
nota2 = int(input("Nota de trimestre 2: "))
nota3 = int(input("Nota de trimestre 3: "))

alumno1 = promedio(nota1, nota2, nota3) # la estoy llamando
print("El promediod del alumno 1 es: "+str(alumno1)) 

