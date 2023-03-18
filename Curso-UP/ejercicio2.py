### RECUPERATORIO = 

# # 1) 
# # En una florería se venden rosas y jazmines, las primeras valen $150 el ramo y las segundas $100. 
# # Se quiere calcular la venta semanal. Se pide:

# # *El total semanal en monto vendido. (Considerar ambos productos).
# # *El producto más vendido en la semana.
# # *La cantidad de rosas vendidas en un día dado


rosas = 150
jazmines = 100
cant_rosas = []
cant_jazmines = []
cont = 0
#dias = [0]


for v in range(7): 
    flores = str(input("Ingrese R para las rosas y J para los jazmines: "))

    if flores == "R":
        cant_rosas.append(rosas)
    if flores == "J":
        cant_jazmines.append(jazmines)

total_semanal = (cant_jazmines + cant_rosas)


def ventas (total_semanal):

    mas_vendido = 0
    if cant_jazmines < cant_rosas:
        mas_vendido += 1
        print("La mayor cantidad de ventas fue de las rosas con: ", cant_rosas)
    if cant_jazmines > cant_rosas:
        mas_vendido += 1
        print("La mayor cantidad de ventas fue de los jazmines con: ", cant_jazmines)

    return mas_vendido


# def posiciones(total_semanal):
    
#     dias = total_semanal[0]
#     acum = 0

while cont < 7:
    int(input("Seleccione el dia de la semana (con numero) en el cual quiere ver que flor se vendio: ", flores[0], flores[1], flores[2], flores[3], flores[4], flores[5]. flores[6], flores[7]))



print(total_semanal)
print(ventas(total_semanal))


