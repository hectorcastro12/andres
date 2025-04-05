import tkinter as tk

# Función que cambia el texto de la etiqueta cuando se hace clic en el botón
def cambiar_texto():
    label.config(text="¡Hola, has hecho clic en el botón!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica de Usuario")
ventana.geometry("400x200")  # Tamaño de la ventana

# Crear un widget Label (etiqueta)
label = tk.Label(ventana, text="¡Bienvenido! Haz clic en el botón.", font=("Arial", 14))
label.pack(pady=20)

# Crear un widget Button (botón)
boton = tk.Button(ventana, text="Haz clic aquí", command=cambiar_texto)
boton.pack(pady=10)

# Ejecutar el bucle de eventos
ventana.mainloop()