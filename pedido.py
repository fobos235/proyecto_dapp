class Pedido:
    pedidos=[]
    productos=[]
    def abrirPedido(self, clave):
        self.clave=clave
        self.fecha=input("Ingresa la fecha")
        self.hora=input("Ingresa la hora")
        self.nombre=input("Ingresa el nombre del cliente")
        self.estatus=input("Ingresa el estatus (Abierto/Cerrado)")
        
    
    def registrarPedido(self, clave):
        objeto=Pedido()
        objeto.abrirPedido(clave)
        self.pedidos.append(objeto)
        print(self.pedidos[0].clave)

    def imprimirPedidos(self):
        for i in range(0, len(self.pedidos)):
            print("\nPedido: ",self.pedidos[i].clave," Fecha: ",self.pedidos[i].fecha," Hora: ",self.pedidos[i].hora," Cliente: ",self.pedidos[i].nombre)

    def addProductosPedido(self, idPedido):
        #Usamos el metodo de impresion de productos y obtenemos productos
        self.id=idPedido
        self.producto=input("Ingresa producto")
        self.cantidad=int(input("Ingresa la cantidad"))
        self.costo=input("costo")
        self.detalle=input("Especifia detalles de la preparación del producto")
    
    def registrarProductosPedido(self):
        decidir=True 
        #Se necesita una variable boleana para validar un while que nos permita añadir los productos a un pedido
        objeto=Pedido()
        objeto.imprimirPedidos() 
        #Para saber a que pedido agregarle producto creamos un objeto Pedido e imprimimos una lista de pedidos
        ids=input("Ingresa la clave del pedido")
        
        for i in range(0, len(self.pedidos)):
            #Cuándo ya sabemos a que pedido agregarle productos comparamos la clave que ya tenemos con la que tienen todos los pedidos
            if self.pedidos[i].clave==ids: 
                #Si esto coincide sabemos que i será la posicion de la lista por lo que verificamos si el estatus está cerrado o abierto en la posicion i
                if self.pedidos[i].estatus=='Cerrado': 
                    #Si encontramos que el pedido está cerrado nuestra variable para entrar al while se hace False
                    decidir=False
        if decidir==False:
            #Si la variable es False no puede entrar en el ciclo y mandará el mensaje de abajo
            print("No pueden agregarse productos a un pedido cerrado")            
        while (decidir):
            print("Agregar Productos al Pedido\n")
            #Una vez que decidir se haya mantenido en True luego de validar, imprime la lista de productos a la vez que los agrega a una nueva lista 
            objeto.addProductosPedido(ids)
            self.productos.append(objeto)
            #Al final no pregunta si deseamos seguir agregando productos al pedido que especificamos
            sino=input("¿Desea continuar agregando productos al pedido ",ids,"? (si/no)")
            if sino == 'no' or sino =='No':
                decidir=False

    def comprar(self):
        for i in range(0, len(self.pedidos)):
            if pedidos[i].estatus == 'Abierto':
                print("\nPedido: ",self.pedidos[i].clave," Fecha: ",self.pedidos[i].fecha," Hora: ",self.pedidos[i].hora," Cliente: ",self.pedidos[i].nombre," Estatus: ",self.pedidos[i].estatus)

        ids=int(input("Ingresa la clave del pedido"))
        if ids > 0 and ids <= len(self.pedidos) or self.pedidos[ids].estatus=='Abierto':
            self.pedidos[ids].estatus='Cerrado'
    
    def imprimirTicket(self, clave):
        
        for i in range (0, len(self.productos)):
            print("")