"""
Definir una clase cliente que almacene un código de cliente y un nombre.
En la clase cliente definir una variable de clase tipo lista que almacene todos los códigos de clientes
que tienen suspendidas sus cuentas corrientes.
"""
class Cliente:
    suspendidos=[]

    def __init__(self, codigo, nombre):
        self.codigo=codigo
        self.nombre=nombre

    def imprimir(self):
        print("Código", self.codigo)
        print("Nombre", self.nombre)
        self.esta_suspendido()
    
    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Está suspendido")
        else:
            print("No está suspendido")
        print("________________________________")
        
    def suspender(self):
        Cliente.suspendidos.append(self.codigo)
    
#Bloque principal
cliente1=Cliente(1, "Carlos")
cliente2=Cliente(2, "Ana")
cliente3=Cliente(3, "Pedro")
cliente4=Cliente(4, "Luís")

cliente2.suspender()
cliente3.suspender()


cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)

