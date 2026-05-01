import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa para subir a repositorio")
ventana.geometry("500x300")  # tamaño más grande para que se vea mejor
ventana.configure(bg="#2C3E50")  # color de fondo elegante

# Crear etiqueta con tipografía mejorada
etiqueta = tk.Label(
    ventana,
    text="Este programa es de Fernanda y Brittany",
    font=("Comic Sans MS", 16, "bold"),  # fuente más divertida, tamaño 16, negrita
    fg="#E74C3C",  # color del texto rojo brillante
    bg="#2C3E50"   # fondo igual que la ventana
)
etiqueta.pack(pady=30)

# Agregar otra etiqueta opcional con colores llamativos
sub_etiqueta = tk.Label(
    ventana,
    text="¡Bienvenido al programa!",
    font=("Arial", 14, "italic"),
    fg="#F1C40F",  # amarillo brillante
    bg="#2C3E50"
)
sub_etiqueta.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()