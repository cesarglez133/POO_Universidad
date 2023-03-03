import tkinter as tk
import tkinter.messagebox as messagebox
from login import Login

class interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Login")

        # Crear widgets
        self.etiquetaCorreo = tk.Label(self.ventana, text="Correo electrónico:")
        self.correo = tk.Entry(self.ventana)
        self.etiquetaPassword = tk.Label(self.ventana, text="Contraseña:")
        self.password = tk.Entry(self.ventana, show="#")
        self.botonLogin = tk.Button(self.ventana, text="Iniciar sesión", command=self.login)

        # Colocar widgets
        self.etiquetaCorreo.grid(      row=0,    column=0,     padx=10,    pady=10)
        self.correo.grid(              row=0,    column=1,     padx=10,    pady=10)
        self.etiquetaPassword.grid(    row=1,    column=0,     padx=10,    pady=10)
        self.password.grid(            row=1,    column=1,     padx=10,    pady=10)
        self.botonLogin.grid(          row=2,    column=1,     padx=10,    pady=10)

    def login(self):
        email = self.correo.get()
        password = self.password.get()
        login = Login(email, password)

        messagebox.showinfo("iii ALERTA !!!", login.login())

if __name__ == "__main__":
    ventana = tk.Tk()
    app = interfaz(ventana)
    ventana.mainloop()
