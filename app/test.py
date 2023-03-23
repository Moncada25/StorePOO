import tkinter as tk


class TiendaPOO:

    def __init__(self, master):
        self.master = master
        master.title("TiendaPOO")

        # Configura el tamaño de la ventana
        width = 620
        height = 380
        x = (master.winfo_screenwidth() // 2) - (width // 2)
        y = (master.winfo_screenheight() // 2) - (height // 2)
        master.geometry(f"{width}x{height}+{x}+{y}")

        # Carga la imagen del gato
        image = tk.PhotoImage(file="tienda.png")
        label = tk.Label(master, image=image)
        label.image = image
        label.pack()

        # Crea un contenedor para los botones
        button_frame = tk.Frame(master)
        button_frame.pack(side="bottom", fill="x", pady=10)

        # Crea los botones
        self.show_button = tk.Button(button_frame, text="Show")
        self.add_button = tk.Button(button_frame, text="Add")
        self.delete_button = tk.Button(button_frame, text="Delete")
        self.show_all_button = tk.Button(button_frame, text="Show all")
        self.show_clients_button = tk.Button(button_frame, text="Show clients")
        self.exit_button = tk.Button(button_frame, text="Exit", command=master.quit)

        # Empaqueta los botones
        self.show_button.pack(side="left", padx=5)
        self.add_button.pack(side="left", padx=5)
        self.delete_button.pack(side="left", padx=5)
        self.show_all_button.pack(side="left", padx=5)
        self.show_clients_button.pack(side="left", padx=5)
        self.exit_button.pack(side="right", padx=5)


root = tk.Tk()
my_gui = TiendaPOO(root)
root.mainloop()
