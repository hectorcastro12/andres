from datetime import datetime
from typing import Dict, List, Tuple, Optional
import json



inventory = {}

def add_product(titulo, autor, categoria, price, counts):
    #Adds a new product to inventory or updates its quantity if it already exists.
    if titulo in inventory:
        inventory[titulo] = (autor, categoria, price, inventory[titulo][1] + counts)
        print(f"{counts} units of {titulo} have been added.")
        
    else:
        inventory[titulo] = (price, counts)
        print(f"\n{counts} Products {titulo} added to inventory.")

def query_product(titulo):
    #Query the details of a product by name.
    if titulo in inventory:
        autor, categoria, price, counts  = inventory[titulo]
        print(f"{titulo}: autor = {autor} categoria = {categoria} Price = ${price}, Quantity = {counts}")
    else:
        print(f"Product {titulo} is not in inventory.")

        #Updates the price of an existing product.

def update_price(titulo, new_price):

    if titulo in inventory:
        counts = inventory[titulo][1]
        inventory[titulo] = (new_price, counts)
        print(f"The price of {titulo} has been updated to ${new_price}.")
    else:
        print(f"The product {titulo} is not in inventory.")

def remove_product(titulo):
    #Removes a product from inventory.
    if titulo in inventory:
        inventory[titulo]
        print(f"Product {titulo} is removed from inventory.")
    else:
        print(f"The product {titulo} is not in inventory.")

def calculate_total_value():
    #Calculates the total inventory value.
    total_value = sum(map(lambda p: p[0] * p[1], inventory.values()))
    print(f"Total inventory value: ${total_value:.2f}")

def main():
        #In this section, there will be a menu to choose from among the options that the inventory system will have.
    while True:
        print("\n--- Inventory system menu ---")
        print("\n(1). Add products ")
        print("\n(2). Query products ")
        print("\n(3). Delete products ")
        print("\n(4). Update products ")
        print("\n(5). Calculate total product value ")
        option = input("\n Enter an option ")
        if option == "1":
            titulo = input("Enter the title of the product ")
            try:
                autor = input("ingrese el nombre del autor")
                categoria = input("📄 ingrese la categoria correspondiente literatura - ciencias- etc : ")
                price = float(input(" Enter the price of the product : "))
                counts = int(input(" enter the quantity of the product : "))
                add_product(titulo, autor, categoria, price, counts)
            except ValueError:
                print("enter correct values")
        elif option == "2":
            titulo = input(" enter the product to query :")
            query_product(titulo)
        elif option == "3":
            titulo = input(" enter the product to update :")
            try:
                new_price = int(input(" enter the price of the product to update :"))
                update_price(titulo, new_price)
            except  ValueError:
                print("enter correct values")
        elif  option == "4":
            titulo = input(" Enter the name of the product to delete: ")
            remove_product(titulo)
        elif option == "5":
            calculate_total_value()
        elif option == "6":
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()