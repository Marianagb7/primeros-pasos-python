import tkinter as tk

class Aplicacion:

    def __init__(self):

        self.ventana1=tk.Tk()
        self.listbox1=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE)
        self.listbox1.grid(column=0, row=0)
        self.listbox1.insert(0, "uvas")
        self.listbox1.insert(1, "naranjas")
        self.listbox1.insert(2, "limón")
        self.listbox1.insert(3, "sandia")
        self.listbox1.insert(4, "melón")
        self.listbox1.insert(5, "durazno")
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)
        self.label1=tk.Label(self.ventana1, text="Seleccionado")
        self.label1.grid(column=0, row=2)
        self.ventana1.mainloop()
    
    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            todos=""
            for posicion in self.listbox1.curselection():
                todos+=self.listbox1.get(posicion)+"\n"
            self.label1.configure(text=todos)

aplicacion=Aplicacion()

