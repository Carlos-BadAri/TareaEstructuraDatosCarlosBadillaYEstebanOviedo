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

    def encolar(self, valor):
        # Encolar agrega un elemento al final de la cola
        nuevo_nodo = NodoCola(valor)

        if self.esVacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo

        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

        self.tamano += 1

    def desencolar(self):
        # Desencolar saca el elemento que está al frente de la cola
        if self.esVacia():
            print("La cola está vacía.")
            return None

        valor_desencolado = self.frente.valor
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        self.tamano -= 1

        return valor_desencolado

    def mostrar(self):

        if self.esVacia():
            print("La cola está vacía.")
            return

        actual = self.frente

        while actual is not None:

            # Usa el método imprimir() de la clase producto
            actual.valor.imprimir()

            print("-" * 20)

            # Avanza al siguiente nodo
            actual = actual.siguiente