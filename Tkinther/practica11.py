from tkinter import Tk, Button, Frame, messagebox

def mostrarMensaje():
    messagebox.showinfo("AVISO", "Presionaste el boton azul")
    messagebox.showerror("Error", "Todo falló con exito")
    print (messagebox.askokcancel("Pregunta", "¿Ella jugó con tu corazón?"))
    print (messagebox.askyesno("Pregunta", "¿Ella jugó con tu corazón?"))
    print (messagebox.askretrycancel("Pregunta", "¿Ella jugó con tu corazón?"))
    print (messagebox.askyesnocancel("Pregunta", "¿Ella jugó con tu corazón?"))
    
#6. Funcion para agregar botones
def agregarBoton():
    botonVerde.config(text="+", bg="green", fg="white")
    botonNuevo=Button(seccion3,text="Nuevo")
    botonNuevo.pack()
    
#1.Instanciando ventana
ventana=Tk()
ventana.title("Ejemplo de 3 frames")
ventana.geometry("600x400")

#2. Agregando frames
seccion1=Frame(ventana,bg="orange")
seccion1.pack(expand=True,fill="both")

seccion2=Frame(ventana,bg="yellow")
seccion2.pack(expand=True,fill="both")

seccion3=Frame(ventana,bg="#7431CA")
seccion3.pack(expand=True,fill="both")

#3. Agregando botones
botonAzul=Button(seccion1,text="Boton 1",fg="blue", bg="green", command=mostrarMensaje)
botonAzul.place(x=60, y=60)


botonNegro=Button(seccion2,text="Boton 2",fg="black")
botonNegro.grid(row=0,column=0)

botonAmarillo=Button(seccion2,text="Boton 3",fg="yellow")
botonAmarillo.grid(row=1,column=1)

botonVerde=Button(seccion3,text="Boton 4",fg="green", command=agregarBoton)
botonVerde.config(width=10,height=2)
botonVerde.pack()

#llamamos al Main (esta parte siempre va hasta abajo)
ventana.mainloop()