class NodoCola:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamano = 0

    def esVacia(self):
        return self.frente is None

    def encolar(self, valor): #Encolar es que agrega un elemento al final de la fila
        nuevo_nodo = NodoCola(valor)
        if self.esVacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo #Final se actualiza para que apunte al nodo reciuente
            self.final = nuevo_nodo
        self.tamano += 1

    def desencolar(self): #saca el elemento de adelante de la fila (el más antiguo)
        if self.esVacia():
            print("La cola está vacía.")
            return None
        valor_desencolado = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:   # si era el único elemento
            self.final = None
        self.tamano -= 1
        return valor_desencolado

    def mostrar(self):
        if self.esVacia():
            print("La cola está vacía.")
            return
        actual = self.frente
        while actual is not None:
            actual.valor.imprimir() # Usa el metodo imprimir() de la clase producto
            print("-" * 20) #este *20 es para imprimer el elemento 20 veces
            actual = actual.siguiente #Avanza