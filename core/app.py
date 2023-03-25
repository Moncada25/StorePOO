from core.store import Store
import tkinter as tk
from tkinter import messagebox

from utils import utils


class App:
    app = Store()
    app.start(True)

    def __init__(self, master):
        self.master = master
        master.title("Store")

        # Configura el tamaño de la ventana
        width = 850
        height = 350
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
        self.show_products = tk.Button(button_frame, text="Show products", command=self.btn_show_products)
        self.show_distributors = tk.Button(button_frame, text="Show distributors", command=self.btn_show_distributors)
        self.show_clients = tk.Button(button_frame, text="Show clients", command=self.btn_show_clients)
        self.add_product = tk.Button(button_frame, text="Add product")
        self.delete_product = tk.Button(button_frame, text="Delete product")
        self.open_chat = tk.Button(button_frame, text="Open chat", command=self.btn_open_chat)
        self.exit_exit = tk.Button(button_frame, text="Exit", command=master.quit)

        # Empaqueta los botones
        self.show_products.pack(side="left", padx=5)
        self.add_product.pack(side="left", padx=5)
        self.delete_product.pack(side="left", padx=5)
        self.show_distributors.pack(side="left", padx=5)
        self.show_clients.pack(side="left", padx=5)
        self.open_chat.pack(side="left", padx=5)
        self.exit_exit.pack(side="left", padx=5)

    def btn_show_products(self):
        messagebox.showinfo("All products", utils.show_list(self.app.product_list, 'products'))

    def btn_show_clients(self):
        messagebox.showinfo("All client", utils.show_list(self.app.client_list, 'clients'))

    def btn_show_distributors(self):
        messagebox.showinfo("All distributors", utils.show_list(self.app.client_list, 'distributors'))

    def btn_open_chat(self):
        messagebox.showinfo("Open chat", "Chat")


root = tk.Tk()
app = App(root)
root.mainloop()
