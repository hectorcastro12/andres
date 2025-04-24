## Entrenamiento Módulo 1 – Semana 1
 
## Sistema de validación de productos
 
#ANDDRES CASTRO - RIWI (CAIMAN)
 

 
#Mensaje de bienvenida
 
print("=" * 60)
 
print("Bienvenidos a la Tienda Tecnológica RIWI".center(60))
 
print("=" * 60)
 
print("*" * 60)
 

 
while True:
 
    #Entrada de datos
 
    nombre_del_producto = input("Ingrese el nombre del producto: ")
 
    precio_unitario = input("Ingrese el precio unitario del producto: ")
 
    cantidad_de_productos = input("Ingrese cantidad de productos adquiridos: ")
 
    pregunta_de_descuento = input("¿El producto tiene descuento? si/no: ")
 

 
    try: 
 
        # Conversión de datos
 
        precio_unitario_float = float(precio_unitario)
 
        cantidad_de_productos_int = int(cantidad_de_productos)
 

 
        # Validación: que el precio y la cantidad sean números y que estos sean positivos
 
        # Si no, muestra error y pide volver a ingresar datos
 
        if precio_unitario_float < 0 or cantidad_de_productos_int < 0:
 
            print("Error: El precio y la cantidad del producto deben ser números positivos.")
 
            continue
 
    except ValueError:
 
            print("Error: El precio y la cantidad de productos deben ser numeros.")
 
            continue    
 

 
    # Cálculo del costo sin descuento
 
    costo_sin_descuento = precio_unitario_float * cantidad_de_productos_int
 

 
    # Valida si hay descuento y si está dentro de rango permitido
 
    if pregunta_de_descuento.lower() == "si":
 
        valor_de_descuento = input("¿Cuánto es el porcentaje de descuento del producto?: ")
 

 
        if '%' in valor_de_descuento:  # Verifica si contiene el carácter '%'
 
            valor_de_descuento = valor_de_descuento.replace('%', '')  # reemplaza todos los '%' por espacio en blanco
 
        try:
 
            valor_de_descuento_float = float(valor_de_descuento)  # conversion de dato
 

 
        #En caso que se ingrese palabras en vez de numeros se muestra error y vuelve a pedir los datos   
 
        except ValueError:
 
            print("Error: El porcentaje de descuento debe ser un número.")
 
            continue
 

 
        # Valida que el descuento esté dentro del rango permitido
 
        if (valor_de_descuento_float >= 0) and (valor_de_descuento_float <= 100):
 
            # Cálculo de descuento
 
            calculo_de_descuento = (valor_de_descuento_float / 100) * precio_unitario_float
 
            descuento_sobre_producto = precio_unitario_float - calculo_de_descuento
 
            costo_total_con_descuento = descuento_sobre_producto * cantidad_de_productos_int
 

 
            #Imprimir en pantalla
 
            print("=" * 60)
 
            print(" " * 60)
 
            #imprime el costo con descuento y organiza a la izquiera y a la derecha el texto
 
            print(f"Producto: {nombre_del_producto}".ljust(30) + f"Costo total: ${costo_total_con_descuento:.2f}".rjust(30)) #se limita el costo a 2 decimales
 

 
            print(" " * 60)
 
            print("¡Gracias por confiar en RIWI!".center(60))
 
            print("=" * 60)
 
            print("Apreciamos tu visita, ¡esperamos verte pronto!".center(60))
 
            break  # Sale del ciclo al final de la operación
 

 
        else:
 
            print("Valor de descuento no válido. Debe estar entre 0 y 100%.")
 

        #else:
 

    elif pregunta_de_descuento.lower() == "no":
 
        #Si no hay descuento, imprime en pantalla
 
        print("=" * 60)
 
        print(" " * 60)

 
        print("=" * 60)
 
        print("Apreciamos tu visita, ¡esperamos verte pronto!".center(60))
 
        print("*" * 60)
 

        break  
 

        break
 

    else:
 

        #En caso que el usuario no indique entre las opciones disponible, se muestra error
 

        #Y vuelve a pedirle los datos
 

        print("Error: debe escoger entre las opciones si / no")
 

        continue