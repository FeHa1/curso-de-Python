## Preguntarle al usuario que tabla quiere aprender

# x = int(input("Ingrese la tabla que quiere aprender: "))

# for i in range(1, 11): 
    
#     valor = i * x
#     print(i, 'x', x, '=',valor)

## Leer 10 valores que ingresa el usuario y los muestre

# x = int(input("Ingrese 10 valores que quiera el usurio: "))
# acum = 0

# for i in range(1, 10):
#     x = int(input("Ingrese 10 valores que quiera el usurio: "))
#     print(x)
#     acum += x
#     #print(acum)
# print(acum)

## Imprimir las tablas del 2 al 10 sin pedirle al usuario nada

for x in range(2, 11):

    for i in range(1, 11):     
    
        valor = i * x
        print(i, 'x', x, '=',valor)
    m = str(input(" ")) # esto es para que el usuario vea las tablas una por una y presione 'enter' para cuando
                        # quiera ver la siguiente
