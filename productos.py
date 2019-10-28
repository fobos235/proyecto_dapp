import prodFunciones as f
class Productos:
    # prod = []
    prods = []

    # def __init__(self):
    def registrar(self):
        productos = f.MetodosProd()
        self.prods.append(productos)      

    def consultar(self):
        valor = input("Ingrese la clave o nombre del producto: ")
        print("CLAVE \tNOMBRE\t \tCOSTO\tCATEGORIA\tDESCRIPCIÓN")
        for i in range(0, len(self.prods)):
            print(self.prods[i].consultar(valor, valor))
    
    def cambiarCosto(self):
        clave = input("INSERTE LA CLAVE DEL PRODUCTO: ")
        for i in range(0, len(self.prods)):
            self.prods[i].modPrecio(clave)

    def inventario(self):
        # Esto no funciona aún
        for i in range(0, len(self.prods)):
            self.inv = self.prods[i]

