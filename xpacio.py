inventario = {}

while True:
    # opcion de ingresar productos
    opcion = input("\nA) agregar producto / B) consultar producto: ").strip().upper()
    
    if opcion == 'A':
        # logica para ingresar nombre, cantidad de productos
        producto = input("Ingrese el nombre del producto: ").strip()
        cantidad = int(input("Ingrese la cantidad del producto: "))
        inventario[producto] = inventario.get(producto, 0) + cantidad
        print(f"Producto '{producto}' agregado con éxito. Cantidad total: {inventario[producto]}")
    
    elif opcion == 'B':
        # LOgica para consultar inventario
        producto = input("Ingrese el nombre del producto a consultar: ").strip()
        if producto in inventario:
            print(f"El producto '{producto}' tiene una cantidad de: {inventario[producto]}")
        else:
            print(f"El producto '{producto}' no está en el inventario.")
    
    else:
        print("Opción no válida. Por favor, elija 'A' o 'B'.")
    
    