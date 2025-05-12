#Ejercicio 1: Contador de positivos
#Plantea un programa que permita ingresar 10 números y cuente cuántos de ellos son mayores que cero.
for i in range(1, 11):
    numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")