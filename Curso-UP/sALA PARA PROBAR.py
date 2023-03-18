# Se quiere gestionar la venta semanal de libros infantiles (7 dias), se tienen dos productos, libros para colorear que tiene un coste de $159 y libro de cuentos $320.     
# Tip: se genera un arreglo para cada tipo de producto. 

# Se pide: 
# Generar una funcion que retorne el dia que menops se vendio, para cada uno de los productos. 
# Mostrar el promedio de ventas de libros para colorear. 
# Mostrar el total vendido en pesos en una semana. Considerando ambos productos. 

libro_colo = 0
libro_cuen = 0
venta_colo = []
venta_cuen = []


def cuentos(libro_cuen, libro_colo):
    cont = 0
    while cont < 7: 
        x = input("Ingrese el libro que quiere, 'C' para el de color y 'F' para el de cuentos: ")

        if x == "C": 
            venta_colo.append(libro_colo)    

        if x == "F": 
            venta_cuen.append(libro_cuen)
            

        x = input("Ingrese el libro que quiere, 'C' para el de color y 'F' para el de cuentos: ")
        cont += 1


cuentos(libro_cuen, libro_colo)

promedio = venta_colo/7 # como tengo que sacar el promedio de los libros para colorear a lo largo de la semana le divido la semana

def menores(venta_colo, venta_cuen):
    
    min = v[0]
    for x in v:
        if x < min: 
            min = v

    return

