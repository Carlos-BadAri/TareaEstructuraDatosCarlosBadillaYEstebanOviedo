from datetime import date #Esta libreria nos sirve para obtener la fecha que tiene la compu y ponerlo en el archivo

class Reporte:

    # Con esta clase vamos a llevar todo lo relacionado
    # con el reporte de los productos.
    # No va a modificar la lista, solo va a leerla.

    def mostrarFrecuenciaPaises(self, lista):

        if lista.listaVacia():
            print("No hay productos en la lista.")
            return

        # Se llama el metodo contarPorPais()
        # para saber la cantidad de productos que existen por pais.
        frecuencia = lista.contarPorPais()

        print("\nFrecuencia de productos por pais de origen:")

        # Recorremos todos los elementos del diccionario.
        # pais representa los paises y cantidad
        # la cantidad de productos.

        paisMayor = ""
        cantidadMayor = 0

        for pais, cantidad in frecuencia.items():

            print(f"{pais}: {cantidad} producto(s)")

            if cantidad > cantidadMayor:
                cantidadMayor = cantidad
                paisMayor = pais

        print(f"\nEl pais del que se importan mas productos es: {paisMayor}")
        print(f"Cantidad de productos: {cantidadMayor}")
        
    def generarReporteRecuperacion(self, lista, nombreArchivo="ReporteRecuperacion.txt"):

        fechaActual = date.today()

        if lista.listaVacia():
            print("No hay productos en la lista, NO se genero el reporte.")
            return

        total = 0

        # open() permite abrir o crear un archivo.
        # "w" significa "write", es decir, escribir.
        # Si el archivo no existe, Python lo crea.
        # Si ya existe, se reemplaza su contenido.
        with open(nombreArchivo, "w") as archivo:

            archivo.write("REPORTE DE RECUPERACION DEL SUPERMERCADO\n")

            archivo.write(f"Fecha: {fechaActual}\n")

            archivo.write("=" * 30 + "\n\n")

            actual = lista.cabeza

            while actual is not None:

                p = actual.valor

                # Calculamos lo que debe recuperar
                # de cada producto:
                # precio * existencias
                subtotal = p.precio * p.existencias

                total += subtotal

                # Escribimos los datos en el archivo.
                archivo.write(f"Producto: {p.nombre} (Id: {p.Id})\n")

                archivo.write(f"    Precio: {p.precio}\n")

                archivo.write(f"    Existencias: {p.existencias}\n")

                archivo.write(f"    Subtotal a Recuperar: {subtotal}\n")

                # Pasamos al siguiente nodo en la lista.
                actual = actual.siguiente

            archivo.write("-" * 30 + "\n")

            # Total contemplando todos los productos.
            archivo.write(f"TOTAL A RECUPERAR: {total}\n")

        # Cuando termina el bloque with,
        # el archivo se cierra automaticamente.
        print(f"Reporte generado correctamente en {nombreArchivo}.")