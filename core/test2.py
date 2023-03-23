import tkinter as tk

root = tk.Tk() # Crear la ventana principal

# Crear una etiqueta para el cuadro de texto
label = tk.Label(root, text="Ingrese su nombre:")

# Crear el cuadro de texto con borde y ancho personalizados
entry = tk.Entry(root, width=50, bd=3)

# Crear el botón con texto personalizado
button = tk.Button(root, text="Enviar nombre")

# Ubicar la etiqueta, el cuadro de texto y el botón en la ventana
label.pack()
entry.pack()
button.pack()

# Mostrar la ventana
root.mainloop()
