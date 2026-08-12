class producto:
    def __init__(self, Id, nombre, precio, pais, existencias):
        self.Id = Id
        self.nombre = nombre
        self.precio = precio
        self.pais = pais
        self.existencias = existencias

    def imprimir(self):
        print("Id: ", self.Id)
        print("Nombre: ", self.nombre)
        print("Precio: ", self.precio)
        print("Pais: ", self.pais)
        print("Existencias: ", self.existencias)