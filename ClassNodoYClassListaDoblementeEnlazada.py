class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def estaVacia(self):
        if self.cabeza is None:
            return True

    def agregarAlInicio(self,valor):
        nuevoNodo= Nodo(valor)

        if self.estaVacia() == True:
            self.cabeza = nuevoNodo
            self.cola = nuevoNodo

        else:
            nuevoNodo.siguiente = self.cabeza
            self.cabeza = nuevoNodo

    def agregarAlFinal(self,valor):
        nuevoNodo=Nodo(valor)

        if self.estaVacia() == True:
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

    def eliminarAlInicio(self):
        if self.estaVacia() == True:
            return -1
        else:
            valorEliminado = self.cabeza.valor
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
            return valorEliminado


    def eliminarAlFinal(self):
        if self.estaVacia() == True:
            return -1
        else:
            valorEliminado = self.cola.valor
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            return valorEliminado

    def eliminarEnPosicion(self,posicion):
        if self.estaVacia() == True:
            return -1
        if posicion == 0:
            return self.eliminarAlInicio()
        if posicion == self.cola:
            return self.eliminarAlFinal()
        else:
            nodoActual = self.cabeza
            for i in range(posicion - 1):
                nodoActual = nodoActual.siguiente
                valorEliminado = nodoActual.valor
            auxiliar = nodoActual.anterior
            auxiliar.siguiente = nodoActual.siguiente
            nodoActual.siguiente.anterior = auxiliar
            return valorEliminado

            