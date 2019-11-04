import productos as p
import pedido as ped

class Principal:
    # prods = []

    def __init__(self):
        self.prods = p.Productos()
        self.pedidos=ped.Pedido()

    def menu(self):

        op = "0"
        while op != "11":
            print("1) Agregar producto")
            print("2) Consultar producto")
            print("3) Modificar costo")
            print("4) Inventario")
            print("5) Abrir Pedido")
            print("6) Registrar Pedido")
            print("7) Añadir productos al pedido")
            print("8) Registrar productos en el pedido")
            print("9) Comprar")
            print("10) Generar ticket")
            print("11) Salir")
            op = input("Opción: ")

            if op == "1":
                self.prods.registrar()
            elif op == "2":
                self.prods.consultar()
            elif op == "3":
                self.prods.cambiarCosto()
            elif op == "4":
                self.prods.inventario()
            elif op == "5":
                clave=input("ingresa la clave: ")
                self.pedidos.abrirPedido(clave)
            elif op=="6":
                self.pedidos.imprimirPedidos()
                clave = input("Ingrese la clave del pedido: ")
                self.pedidos.registrarPedido(clave)
            elif op=="7":
                self.pedidos.imprimirPedidos()
                idPedido=input("Ingresa clave del pedido: ")
                self.pedidos.addProductosPedido(idPedido)
            elif op=="8":
                self.pedidos.registrarProductosPedido()
            elif op=="9":
                self.pedidos.comprar()
            elif op=="10":
                clave=input("ingrese la clave")
                self.pedidos.imprimirTicket(clave)
            elif op == "11":
                exit()

pri = Principal()
pri.menu()
