class MetodosProd:
    def __init__(self):
        self.clave = input("Clave del producto: ")
        self.nombre = input("Nombre del producto: ")
        self.costo = float(input("Costo: "))
        self.categoria = input("Categoría del producto: ")
        self.descripcion = input("Descripción del producto: ")

    def consultar(self, nombre = "", clave = ""):
        if self.nombre == nombre:
            return self.clave + ") " + self.nombre + "\t$"+ str(self.costo) + "\t" + self.categoria + "\t" +self.descripcion
        elif self.clave == clave:
            return self.clave + ") " + self.nombre + "\t$"+ str(self.costo)+ "\t" + self.categoria + "\t" +self.descripcion

    def modPrecio(self, clave):
        if self.clave == clave:
            costo = float(input("Nuevo costo: "))
            print("Costo actualizado\n")
        else:
            print("No se encontró el producto\n")
    
    