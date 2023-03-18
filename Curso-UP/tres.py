# Operadores 
# De comparacion: <, >, <=, >=, == (operador igual)
# Logico: are, or, not 

# boolean: True / False

variable = 10 # operador asignado
nombre = "pepe"

#user = input("Ingresar usuario: ")
#password = input("Ingresar password: ")

# Si user es igual a pepe y password es igual a 1234 mostrar bienvenido user
# Si no mostrar usted no es pepe.

#if user == "pepe" and password == "1234":
 #   print("Bienvenido, " + user)
#else:
 #   print("Usted no es pepe")

#print("hola mundo")

# Si es mayor de edad o VIP puede pasar

edad = int(input("Ingrese su edad: "))
VIP = bool(input("¿Es usted vip? True/False: "))

if edad >= 18 or VIP == True: # el ¨or¨ es menos restrictivo entonces hay que tener cuidado al usarlo
    print("Usted puede pasar")
else: 
    print("Fuera de aca")

