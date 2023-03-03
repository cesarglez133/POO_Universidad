import tkinter as tk
import tkinter.messagebox as messagebox


class login:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Login")

        # Crear widgets
        self.etiquetaCorreo = tk.Label(self.ventana, text="Correo electrónico:")
        self.correo = tk.Entry(self.ventana)
        self.etiquetaPassword = tk.Label(self.ventana, text="Contraseña:")
        self.password = tk.Entry(self.ventana, show="~")
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

        if email == "" or password == "":
            tk.messagebox.showerror("Error", "Por favor ingrese su correo y contraseña")
        elif email == "upq@edu.com" and password == "cardenal":
            tk.messagebox.showinfo("Bienvenido", f"Bienvenido {email}")
        else:
            tk.messagebox.showerror("Error", "El correo o la contraseña son incorrectos")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = login(ventana)
    ventana.mainloop()
