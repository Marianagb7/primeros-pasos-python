import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1, text="Esta de acuerdo con los términos y condiciones", variable=self.seleccion, command=self.cambiaremosestado)
        self.check1.grid(column=0, row=0)
        self.boton1=tk.Button(self.ventana1, text="Entrar", state="disable", command=self.ingresar)
        self.boton1.grid(column=0, row=3)
        self.ventana1.mainloop()
    
    def cambiaremosestado(self):
        if self.seleccion.get()==1:
            self.boton1.configure(state="normal")
        if self.seleccion.get()==0:
            self.boton1.configure(state="disabled")

    def ingresar(self):
        self.ventana1.title("Ingresando...")

apliacacion1=Aplicacion()