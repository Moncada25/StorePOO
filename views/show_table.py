import tkinter as tk
from tkinter import ttk


def show_table(objetos, ventana_padre, titulo="Tabla"):
    # Crear nueva ventana
    ventana_tabla = tk.Toplevel(ventana_padre)
    ventana_tabla.title(titulo)

    # Ocultar ventana padre
    ventana_padre.withdraw()

    # Obtener tamaño de pantalla
    ancho_pantalla = ventana_padre.winfo_screenwidth()
    alto_pantalla = ventana_padre.winfo_screenheight()

    # Calcular posición de la ventana de la tabla
    ancho_ventana = 600
    alto_ventana = 400
    x_ventana = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y_ventana = (alto_pantalla // 2) - (alto_ventana // 2)

    # Configurar tamaño y posición de la ventana de la tabla
    ventana_tabla.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, x_ventana, y_ventana))

    # Definir estilo personalizado
    estilo = ttk.Style()
    estilo.configure("mi_estilo.Treeview", font=("Times New Roman", 16))

    # Crear Treeview
    treeview = ttk.Treeview(ventana_tabla, style="mi_estilo.Treeview")

    # Agregar columnas
    # Se asume que todos los objetos tienen las mismas propiedades
    # y que las propiedades son representadas por los nombres de las columnas
    columnas = list(objetos[0].__dict__.keys())
    treeview["columns"] = columnas
    treeview.column("#0", anchor=tk.CENTER, width=50, minwidth=50)
    treeview.heading("#0", text="ID")
    for col in columnas:
        treeview.column(col, anchor=tk.CENTER)
        treeview.heading(col, text=col.title())  # Convertir el nombre de la propiedad a título

    # Agregar filas
    indice = 1  # Variable para generar ids consecutivos
    for obj in objetos:
        valores = [getattr(obj, col) for col in columnas]
        treeview.insert("", tk.END, text=str(indice), values=valores)
        indice += 1

    # Centrar el contenido de las columnas
    for col in columnas:
        treeview.column(col, anchor=tk.CENTER)

    # Mostrar tabla
    treeview.pack(expand=True, fill="both")

    # Función para cerrar la tabla
    def cerrar_tabla():
        ventana_tabla.destroy()
        ventana_padre.deiconify()

    # Agregar botón para cerrar la tabla
    boton_cerrar = tk.Button(ventana_tabla, text="Cerrar", command=cerrar_tabla)
    boton_cerrar.pack()

    # Configurar cierre de ventana
    ventana_tabla.protocol("WM_DELETE_WINDOW", cerrar_tabla)
