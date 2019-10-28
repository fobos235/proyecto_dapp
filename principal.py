import productos as p

class Principal:
    # prods = []

    def __init__(self):
        self.prods = p.Productos()

    def menu(self):
        
        op = "0"
        while op != "5":
            print("1) Agregar")
            print("2) Consultar producto")
            print("3) Modificar costo")
            print("4) Inventario")
            op = input("Opción: ")

            if op == "1":
                prod = p.Productos()
                self.prods.append(prod)
            elif op == "2":
                val = input("Ingrese clave o nombre del producto: ")
                for i in range (0, len(self.prods)):
                    print(self.prods[i].consultar)
            elif op == "3":
                val = input("Ingrese clave del producto a modificar: ")
                for i in range (0, 0, len(self.prods)):
                    self.prods[i].modPrecio(val)
            elif op == "4":
                for i in range (0, len(self.prods)):
                    print(self.prods.inventario())

pri = Principal()
pri.menu()
                    