#Este código corresponde a un cuestionario.
#Se evalúan 3 preguntas, registra respuestas y muestra resumen al finalizar.
# espacio de importaciones  
import os #esta libreria sirve para limpiar la consola

def clear():
    '''
    Esta fucion la utilizo para limpiar la consola en
    linux o windows, se utiliza llamando os.system()
    '''
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")
# Mensaje de bienvenida
# 60 caracteres será la longitud estándar de cada línea

print("")
print("=" * 60) #se multiplica para respetar la longitud estándar

print("BIENVENIDO CODER".center(60))
print("=" * 60)

nombre_de_usuario= input("Ingrese su nombre: ")

print (" ")
print(f"{nombre_de_usuario}, Vas a realizar la prueba de conocimiento general")
print("Las preguntas son de opción múltiple y solo puedes escoger")
print("una respuesta válida")
print (" ")

#comenzar aqui la parte del codigo de las preguntas

respuestas = ["A", "B", "C", "D"]
contador_correctas = 0
contador_incorrectas = 0

# Pregunta 1
while True:
    print("Pregunta 1: ¿De que color es la caja negra de los aviones?")
    print("A) Naranja")
    print("B) negra")
    print("C) azul")
    print("D) gris")

    respuesta_correcta_1 = "A"
    print("")
    respuesta_usuario_1 = input("Ingrese su respuesta (A, B, C, D): ").upper()

    if respuesta_usuario_1 in respuestas:
        break
    else:
        print("Elija una opción válida (A, B, C, D)")

print(f"Respuesta guardada: {respuesta_usuario_1}")

if respuesta_usuario_1 == respuesta_correcta_1:
    contador_correctas += 1
else: 
    contador_incorrectas += 1

clear()
# Pregunta 2
while True:
    print("\nPregunta 2: Si en una carrera usted adelanta al segundo ")
    print("lugar justo antes de cruzar la meta, ¿En qué posición ")
    print("terminaría la carrera?")
    print("")
    print("A) Primer lugar")
    print("B) Segundo lugar")
    print("C) Tercer lugar")
    print("D) Cuarto lugar")

    respuesta_correcta_2 = "B"
    print("")
    respuesta_usuario_2 = input("Ingrese su respuesta (A, B, C, D): ").upper()

    if respuesta_usuario_2 in respuestas:
        break
    else:
        print("Elija una opción válida (A, B, C, D)")

print(f"Respuesta guardada: {respuesta_usuario_2}")

if respuesta_usuario_2 == respuesta_correcta_2:
    contador_correctas += 1
else: 
    contador_incorrectas += 1

clear()
# Pregunta 3
while True:
    print("\nPregunta 3: ¿Cuál es el rol en Scrum encargado de maximizar ")
    print("el valor del producto y gestionar el Product Backlog?")
    print("")
    print("A) Scrum Master")
    print("B) Product Owner")
    print("C) Development Team")
    print("D) Project Manager")

    respuesta_correcta_3 = "B"
    print("")
    respuesta_usuario_3 = input("Ingrese su respuesta (A, B, C, D): ").upper()

    if respuesta_usuario_3 in respuestas:
        break
    else:
        print("Elija una opción válida (A, B, C, D)")

print(f"Respuesta guardada: {respuesta_usuario_3}")

if respuesta_usuario_3 == respuesta_correcta_3:
    contador_correctas += 1
else: 
    contador_incorrectas += 1
clear()
### Resumen de respuesta usuario

print("")
print("=" * 60) #se multiplica para respetar la longitud estándar
print(f"RESUMEN DE RESPUESTAS DE {nombre_de_usuario}: ".center(60))
print("=" * 60)

print(f"\nRespuestas correctas ✅ : {contador_correctas}")
print(f"Respuestas Incorrectas ❌ : {contador_incorrectas}\n")

print("RESPUESTAS INCORRECTAS:")

if respuesta_usuario_1 != respuesta_correcta_1:
    print(f"Pregunta 1. Respuesta correcta: {respuesta_correcta_1}, su respuesta: {respuesta_usuario_1}")

if respuesta_usuario_2 != respuesta_correcta_2:
    print(f"Pregunta 2. Respuesta correcta: {respuesta_correcta_2}, su respuesta: {respuesta_usuario_2}")

if respuesta_usuario_3 != respuesta_correcta_3:
    print(f"Pregunta 3. Respuesta correcta: {respuesta_correcta_3}, su respuesta: {respuesta_usuario_3}")

print("")