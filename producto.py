#PROYECTO5
import funciones as f
class Producto:
    productos=[]
    
    def registrar_pelicula(self):
        prod=f.Funcion()
        self.productos.append(prod)

    def verInventario(self):
        print("\nInventario: ")
        for i in range(0, len(self.productos)):
            print("\nNombre: "+self.productos[i].nom)
            print("Clave: "+self.productos[i].clave)
            print("Costo: "+self.productos[i].costo)
            print("Categoría: " + self.productos[i].categ)
            print("Descripción: " + self.productos[i].desc)
   
    def modificarCosto(self):
        print()
   
    def menu(self):
        while(True):
            print("\n1) Registrar Producto")
            print("2) Ver inventario")
            print("3) Buscar producto")
            print("4) Actualizar costo del producto")
            print("10) Salir\n")
            op=int(input("Ingresa una opción: "))
            if op==1:
                self.registrar_pelicula()
            elif op==2:
                self.verInventario()
            elif op==3:
                a=True
                while a==True:
                    print("\n1) Buscar por nombre")
                    print("2) Buscar por clave")
                    print("3) Regresar\n")
                    o=int(input("Ingresa una opción: "))
                    if o==1:
                        self.busqueda=input("Nombre del producto: ")
                        for i in range(0, len(self.productos)):
                            self.resultado=self.productos[i].consultar(self.busqueda)
                            if (self.resultado!=None):
                                print("\n"+ self.resultado)
                            else:
                                print("\nNombre no encontrado!")
                    elif o==2:
                        self.busqueda=input("Clave del producto: ")
                        for i in range(0, len(self.productos)):
                            self.resultado=self.productos[i].consultarClave(self.busqueda)
                            if (self.resultado!=None):
                                print("\n"+ self.resultado)
                            else:
                                print("\nClave no encontrada!")
                    elif o==3:
                        a=False
            elif op==4:
                self.busqueda=input("Clave del producto: ")
                for i in range(0, len(self.productos)):
                    self.resultado=self.productos[i].consultarClave(self.busqueda)
                    if(self.resultado!=None):
                        cost=input("Nuevo precio: ")
                        self.productos[i].modificarCosto(cost)
                else:
                    self.ciclo=False
            elif op==10:
                break

print()
obj=Producto()
obj.menu()