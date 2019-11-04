class Funcion:
    def __init__(self):
        self.clave=input("Ingresa la clave: ")
        self.nom=input("Ingresa el nombre: ")
        self.costo=input("Ingresa el costo: ")
        self.categ=input("Ingresa la categoria (comida/bebida): ")
        self.desc=input("Descripción: ")

    def consultar(self,nombre):
        if (self.nom==nombre):
            return "Clave: "+ self.clave + " Costo: " + self.costo + " Categoría: " + self.categ + " Descripción: " + self.desc

    def consultarClave(self,clave):
        if (self.clave==clave):
            return "Nombre: "+ self.nom + " Costo: " + self.costo + " Categoría: " + self.categ + " Descripción: " + self.desc
    
    def ModificarCosto(self,cost):
    
            self.costo=cost

