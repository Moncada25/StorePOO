from core.store import Store
import tkinter as tk
from tkinter import messagebox
from utils import utils


class App:
    app = Store()
    app.start()

    def __init__(self, master):
        self.master = master
        master.title("Store")

        # Configura el tamaño de la ventana
        width = 620
        height = 380
        x = (master.winfo_screenwidth() // 2) - (width // 2)
        y = (master.winfo_screenheight() // 2) - (height // 2)
        master.geometry(f"{width}x{height}+{x}+{y}")

        # Carga la imagen del gato
        image = tk.PhotoImage(file="../assets/store.png")
        label = tk.Label(master, image=image)
        label.image = image
        label.pack()

        # Crea un contenedor para los botones
        button_frame = tk.Frame(master)
        button_frame.pack(side="bottom", fill="x", pady=10)

        # Crea los botones
        self.show_button = tk.Button(button_frame, text="Show", command=self.btn_show_products)
        self.add_button = tk.Button(button_frame, text="Add")
        self.delete_button = tk.Button(button_frame, text="Delete")
        self.show_all_button = tk.Button(button_frame, text="Show all")
        self.show_clients_button = tk.Button(button_frame, text="Show clients", command=self.btn_show_clients)
        self.exit_button = tk.Button(button_frame, text="Exit", command=master.quit)

        # Empaqueta los botones
        self.show_button.pack(side="left", padx=5)
        self.add_button.pack(side="left", padx=5)
        self.delete_button.pack(side="left", padx=5)
        self.show_all_button.pack(side="left", padx=5)
        self.show_clients_button.pack(side="left", padx=5)
        self.exit_button.pack(side="right", padx=5)

    def btn_show_products(self):
        messagebox.showinfo("All products", utils.show_list(self.app.product_list, 'products'))

    def btn_show_clients(self):
        messagebox.showinfo("All client", utils.show_list(self.app.client_list, 'clients'))

root = tk.Tk()
my_gui = App(root)
root.mainloop()
