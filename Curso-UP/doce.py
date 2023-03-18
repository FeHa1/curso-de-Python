# Se quieren guardar los datos de ventas diarias de un kiosco.
# Se pide cargar la venta semanal.
# Crear una funcion que retorne el dia que menos se vendio. 

valores = []
cont = 0 

while cont < 7:
    valores.append(int(input("Ingrese un valor: "))) # el termino ".append" me permite agregar todos los elementos que yo quiera.
    cont += 1

minimo = lista[0]

for v in valores: # variables globales: son funciones declaradas dentro del codigo principal. No se usan variables dentro de las funciones no declaradas localmente.
    if v < minimo: # variable local: es la variable que defino dentro de una funcion. Minimo es la variable local de la funcion valores.
        minimo = v
print(minimo)

## otro ejemplo

cont = 0
valores = [] # arreglo vacio 

while cont < 7:
    valores.append(int(input("Ingrese un valor: ")))
    cont += 1

def menor(valores):
    minimo = valores[0]
    for v in valores:
        if v < minimo:
            minimo = v
    return(minimo) # el return siempre debe estar dentro del "def"

print(menor(valores))



# Crear una funcion que cargue un array con nombres de colores
# colores = [rojo, amarillo, blanco, azul]
# Generar una funcion que devuelva el nombre de la combinacion de colores pasandole dos indices
# Que los mezclen (celeste, naranja, verde)

colores = ["rojo", "amarillo", "blanco", "azul"]

m = 0

def mezcla(colores, c1, c2):
    m = "Elija una combinacion valida"

    if (c1 == 0 and c2 == 1) or (c1 == 1 and c2 == 0): # los numeros representan las posiciones de los datos de la lista
        m = "naranja"
    if (c1 == 2 and c2 == 3) or (c1 == 3 and c2 == 2):
        m = "celeste"
    if (c1 == 1 and c2 == 3) or (c1 == 3 and c2 == 1):
        m = "verde"
    
    return m

resultado = mezcla(colores, c1, c2)
print(resultado)