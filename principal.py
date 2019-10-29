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
            print("5) Salir")
            op = input("Opción: ")

            if op == "1":
                self.prods.registrar()
            elif op == "2":
                self.prods.consultar()
            elif op == "3":
                # val = input("Ingrese clave del producto a modificar: ")
                self.prods.cambiarCosto()
            elif op == "4":
                self.prods.inventario()
            elif op == "5":
                exit()

pri = Principal()
pri.menu()
                    