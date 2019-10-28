class ProdVentas:
    # prod = []
    prods = dict()

    def __init__(self):
        self.clave = input("Clave del producto: ")
        self.nombre = input("Nombre del producto: ")
        self.costo = float(input("Costo: "))
        self.categoria = input("Categoría del producto: ")
        self.descripcion = input("Descripción del producto: ")

    def consultar(self, nom, clv):
        if self.nombre == nom or self.clave == clv:
            return self.clave + ") " + self.nombre + "\t: $"+ self.costo + "\t" + self.categoria + "\t" +self.descripcion

    def modPrecio(self, clv):
        if self.clave == clv:
            costo = float(input("Nuevo costo: "))


