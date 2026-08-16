class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0

    def listaVacia(self):
        return self.cabeza is None

#Metodos Agregar
    def agregarAlInicio(self,valor):
        nuevo_nodo=Nodo(valor)
        if self.listaVacia():
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            nuevo_nodo.siguiente=self.cabeza
            self.cabeza.anterior=nuevo_nodo
            self.cabeza=nuevo_nodo
        self.tamano+=1

    def agregarAlFinal(self,valor):
        nuevo_nodo = Nodo(valor)
        if self.listaVacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamano += 1

    def agregarEnPosicion(self, valor, posicion):
        if posicion < 0 or posicion > self.tamano:
            print("Posición inválida.")
            return
        if posicion == 0:
            self.agregarAlInicio(valor)
        elif posicion == self.tamano:
            self.agregarAlFinal(valor)
        else:
            nuevo_nodo = Nodo(valor)
            nodoActual = self.cabeza
            for i in range(posicion - 1):
                nodoActual = nodoActual.siguiente
            nuevo_nodo.siguiente = nodoActual.siguiente
            nuevo_nodo.anterior = nodoActual
            nodoActual.siguiente.anterior = nuevo_nodo
            nodoActual.siguiente = nuevo_nodo
            self.tamano += 1

#Metodos Eliminar
    def eliminarAlInicio(self):
        if self.listaVacia():
            print("La lista esta vaciua")
            return None
        valor_eliminado = self.cabeza.valor
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        self.tamano -= 1
        return valor_eliminado

    def eliminarAlFinal(self):
        if self.listaVacia():
            print("La lista esta vaciua")
            return None
        valor_eliminado = self.cola.valor
        if self.cabeza != self.cola: #Si hay muchos elementos en la lista
            self.cola=self.cola.anterior
            self.cola.siguiente=None
            self.tamano-=1
        else: # Si solo hay un nodo en la lista
            self.cabeza=None
            self.cola=None
            self.tamano-=1
        return valor_eliminado

    def eliminarEnPosicion(self,posicion):
        if self.listaVacia():
            print("La lista esta vacia")
            return None
        if posicion == 0:
            return self.eliminarAlInicio()
        elif posicion == self.tamano - 1:
            return self.eliminarAlFinal()
        else:
            nodoActual = self.cabeza
            for i in range(posicion):
                nodoActual = nodoActual.siguiente
            valor_eliminado = nodoActual.valor
            nodoActual.anterior.siguiente = nodoActual.siguiente
            nodoActual.siguiente.anterior = nodoActual.anterior
            self.tamano -= 1
            return valor_eliminado

    def eliminarProductoPorID(self, Id):
            if self.listaVacia():
                print("La lista está vacía.")
                return None
            actual = self.cabeza
            while actual:
                if actual.valor.Id == Id:
                    #si es el primero
                    if actual == self.cabeza:
                        return self.eliminarAlInicio()
                    #si es el ultimo
                    if actual == self.cola:
                        return self.eliminarAlFinal()
                    #si esta en medio, reconectamos los nodos vecinos
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    self.tamano -= 1
                    return actual.valor
                actual = actual.siguiente
            return None #No se encontró
    
 #Metodos Buscar   
   
    def buscarIDProducto(self, Id):
        if self.listaVacia():
            print("La lista está vacía.")
            return None
        actual = self.cabeza
        while actual:
            if actual.valor.Id == Id:
                return actual.valor
            actual = actual.siguiente
        return None

#Crear metodo para pasar de una lista a una cola
