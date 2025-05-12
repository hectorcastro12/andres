
# Definir dos listas
#claves = ["nombre", "edad", "ciudad"]
#valores = ["Ana", 28, "Barcelona"]

# Crear un diccionario vacío
#diccionario = {}

# Usar un bucle para agregar pares clave-valor al diccionario
#for i in range(len(claves)):
#    diccionario[claves[i]] = valores[i]

# Mostrar el diccionario resultante
#print("Diccionario creado:", diccionario)

# Pedir una palabra al usuario
#palabra = input("Introduce una palabra: ")

# Crear un diccionario para almacenar la frecuencia de letras
#frecuencia_letras = {}

# Contar la frecuencia de cada letra
#for letra in palabra:
#    if letra in frecuencia_letras:
#        frecuencia_letras[letra] += 1
#    else:
#        frecuencia_letras[letra] = 1

# Mostrar el diccionario con la frecuencia de letras
#print("Frecuencia de letras:", frecuencia_letras)


# Definir un diccionario de frutas y colores
frutas_colores = {
    "manzana": "rojo",
    "platano": "amarillo",
    "pera": "verde",
    "naranja": "naranja"
}

# Pedir al usuario una fruta
fruta = input("Introduce el nombre de una fruta: ")

# Verificar si la fruta está en el diccionario
if fruta in frutas_colores:
    print(f"El color de la {fruta} es: {frutas_colores[fruta]}")
else:
    print("Esa fruta no está en el diccionario.")
    
    
# Definir un diccionario de productos y precios
productos = {
    "pan": 1.20,
    "leche": 0.99,
    "huevos": 2.50
}

# Pedir al usuario el nombre del producto y el nuevo precio
producto = input("Introduce el nombre del producto: ")
precio = float(input(f"Introduce el nuevo precio de {producto}: "))

# Actualizar el precio o agregar el producto
productos[producto] = precio

# Mostrar el diccionario actualizado
print("Diccionario de productos y precios actualizado:", productos)

# Definir dos diccionarios
diccionario1 = {"a": 1, "b": 2, "c": 3}
diccionario2 = {"b": 4, "d": 5}

# Combinar los dos diccionarios manualmente
for clave, valor in diccionario2.items():
    diccionario1[clave] = valor

# Mostrar el diccionario combinado
print("Diccionario combinado:", diccionario1)