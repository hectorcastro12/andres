# Diccionario para almacenar los productos
inventario = {}

def agregar_producto(nombre, precio, cantidad):
    #Añade un nuevo producto al inventario o actualiza su cantidad si ya existe.
    if nombre in inventario:
        inventario[nombre] = (precio, inventario[nombre][1] + cantidad)
        print(f"Se han añadido {cantidad} unidades de {nombre}.")
    else:
        inventario[nombre] = (precio, cantidad)
        print(f"Producto {nombre} agregado al inventario.")

def consultar_producto(nombre):
    #Consulta los detalles de un producto por su nombre.
    if nombre in inventario:
        precio, cantidad = inventario[nombre]
        print(f"{nombre}: Precio = ${precio}, Cantidad = {cantidad}")
    else:
        print(f"El producto {nombre} no se encuentra en el inventario.")

def actualizar_precio(nombre, nuevo_precio):
    #Actualiza el precio de un producto existente.
    if nombre in inventario:
        cantidad = inventario[nombre][1]
        inventario[nombre] = (nuevo_precio, cantidad)
        print(f"El precio de {nombre} ha sido actualizado a ${nuevo_precio}.")
    else:
        print(f"El producto {nombre} no se encuentra en el inventario.")

def eliminar_producto(nombre):
    #Elimina un producto del inventario.
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto {nombre} eliminado del inventario.")
    else:
        print(f"El producto {nombre} no se encuentra en el inventario.")

def calcular_valor_total():
    #Calcula el valor total del inventario.
    valor_total = sum(map(lambda p: p[0] * p[1], inventario.values()))
    print(f"Valor total del inventario: ${valor_total:.2f}")

def mostrar_inventario():
    #Muestra todos los productos en el inventario.
    if inventario:
        print("Inventario:")
        for nombre, (precio, cantidad) in inventario.items():
            print(f"{nombre}: Precio = ${precio}, Cantidad = {cantidad}")
    else:
        print("El inventario está vacío.")

def menu():
    #Muestra el menú principal y gestiona las opciones del usuario.
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio de producto")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Mostrar inventario")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            try:
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                agregar_producto(nombre, precio, cantidad)
            except ValueError:
                print("Por favor, ingrese valores válidos para el precio y la cantidad.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a consultar: ")
            consultar_producto(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            try:
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                actualizar_precio(nombre, nuevo_precio)
            except ValueError:
                print("Por favor, ingrese un valor válido para el nuevo precio.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        elif opcion == "5":
            calcular_valor_total()
        elif opcion == "6":
            mostrar_inventario()
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    menu()