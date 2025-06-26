# 1. Gestión del inventario
# • Registrar, consultar, actualizar y eliminar productos.
# • Cada producto debe tener: título, autor, categoría, precio, cantidad en stock.

# • El sistema debe iniciar con al menos 5 productos pre-cargados.

from datetime import datetime
from typing import Dict, List, Tuple, Optional
import json


# Constants
MIN_STOCK = 0
MIN_PRICE = 0.01
MIN_QUANTITY = 1
MAX_DISCOUNT = 100.0


inventario= {}


# Función para registrar un estudiante
def registrar_producto():
    name_prod = input("Ingrese el nombre del producto : ")
    if name_prod in inventario:
        print("⚠️ Ya existe un libro con ese nombre.")
        return

    nombre = input("Ingrese el nombre del estudiante: ")
    try:
        edad = int(input("Ingrese la edad del estudiante: "))
        notas = []
        for i in range(3):
            nota = float(input(f"Ingrese la nota {i+1} (0 a 5): "))
            while nota < 0 or nota > 5:
                nota = float(input("⚠️ Nota inválida. Intente de nuevo (0 a 5): "))
            notas.append(nota)
    except ValueError:
        print("❌ Error: Ingrese valores válidos (edad entera y notas numéricas).")
        return

    inventario[name_prod] = {
        "nombre": nombre,
        "edad": edad,
        "notas": notas
    }
    print(f"✅ Estudiante {nombre} registrado exitosamente.")
    
    
    # ================== VALIDATION FUNCTIONS ==================

    def _validate_product_data(self, product_id: str, title: str, author: str,
                              category: str, price: float, stock: int) -> bool:
        """Validate product data before adding/updating"""
        if not product_id or not product_id.strip():
            print("Error: Product ID cannot be empty!")
            return False
        
        if not title or not title.strip():
            print("Error: Title cannot be empty!")
            return False
        
        if not author or not author.strip():
            print("Error: Author cannot be empty!")
            return False
        
        if not category or not category.strip():
            print("Error: Category cannot be empty!")
            return False
        
        if not isinstance(price, (int, float)) or price < MIN_PRICE:
            print(f"Error: Price must be at least ${MIN_PRICE}!")
            return False
        
        if not isinstance(stock, int) or stock < MIN_STOCK:
            print(f"Error: Stock must be at least {MIN_STOCK}!")
            return False
        
        return True

    def _validate_sale_data(self, customer_id: str, product_id: str,
                           quantity: int, custom_discount: float) -> bool:
        """Validate sale data before processing"""
        if not customer_id or not customer_id.strip():
            print("Error: Customer ID cannot be empty!")
            return False
        
        if product_id not in self.inventory:
            print(f"Error: Product ID {product_id} not found in inventory!")
            return False
        
        if not isinstance(quantity, int) or quantity < MIN_QUANTITY:
            print(f"Error: Quantity must be at least {MIN_QUANTITY}!")
            return False
        
        if not isinstance(custom_discount, (int, float)) or custom_discount < 0 or custom_discount > MAX_DISCOUNT:
            print(f"Error: Custom discount must be between 0 and {MAX_DISCOUNT}%!")
            return False
        
        return True