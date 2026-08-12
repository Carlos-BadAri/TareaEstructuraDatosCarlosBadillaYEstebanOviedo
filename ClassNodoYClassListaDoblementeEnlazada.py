class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregarAlInicio(self,valor):
        nuevoNodo= Nodo(valor)

        if self.cabeza is None:
            self.cabeza = nuevoNodo
            self.cola = nuevoNodo

        else:
            nuevoNodo.siguiente = self.cabeza
            self.cabeza = nuevoNodo

    def agregarAlFinal(self,valor):
        nuevoNodo=Nodo(valor)

        if self.cabeza is None:
            self.cabeza = nuevoNodo
            self.cola = nuevoNodo
        else:
            self.cola.siguiente = nuevoNodo
            self.cola = nuevoNodo

    def agregarEnPosicion(self,valor,posicion):
        nuevoNodo=Nodo(valor)

        if posicion == 0:
            self.agregarAlInicio(valor)
        if posicion == self.cola:
            self.agregarAlFinal(valor)
        else:
            nodoActual = self.cabeza
            for i in range(posicion):
                nodoActual = nodoActual.siguiente

        auxiliar = nodoActual.anterior

        nuevoNodo.siguiente = nodoActual
        nuevoNodo.anterior = auxiliar
        auxiliar.siguiente = nuevoNodo
        nodoActual.anterior = nuevoNodo