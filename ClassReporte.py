class reporte:
     #Con ests clase vamos a llevar todo lo relacionado 
     #con el reporte de los productos. No va a modificar la lista solo 
     #va a leerla.

     def mostrarFrecuenciaPaises(self, lista):
        if lista.listaVacia():
            print("No hay productos en la lista.")
            return
        #Se llama el metodo contarPorPais() para quie nos devuelva y asi saber
        # la cantidad de productos que existen por pais.
        frecuencia = lista.contarPorPais()
    print("\nFrecuncia de productos por pais de origen: ")
    #Recorremos todos los elementos del diccionario, pais representa los paises y cantidad
    #la existencia de los mismos.
    for pais, cantidad in frecuencia.itrems():
        print(f"{pais}: {cantidad} producto(s)")

    def generarReporteRecuperacion(self, lista, nombreArchivo="ReporteRecuperacion.txt"):
        if lista.listavacia():
            print("No hay productos en la lista, NO se genero el reporte.")
            return
        total = 0 
        
        with open(nombreArchivo, "w") as archivo:
            archivo.write("REPORTE DE RECUPERACION DEL SUPERMERCADO\n")
            archivo.write("="* 30 + "\n\n")
        #open() permite abrir o crear un archivo.
        # "w" significa "write", es decir, escribir.
        # Si el archivo no existe, Python lo crea. Si ya existe, se reemplaza su contenido.
            actual= lista.cabeza
            while actual is not None:
                p = actaual.valor
                #ponemos lo que debe recuperar de cada producto
                #como precio * extistencias

                subtotal= p.precio * p.existencias
                total += subtotal
                
                #Escribimos los datos en el archivo.
                archivo.write(f"Producto: {p.nombre} (Id: {p.Id})\n")
                archivo.write(f"    Precio: {p.precio}\n")
                archivo.write(f"    Existencias: {p.existencias}\n")
                archivo.write(f"    Subtotal a Recuperar: {subtotal}\n") 

                actual = actual.siguiente  #Pasamos al siguiente nodo en la lista.

            archivo.write("-"*30+"\n")
            archivo.write(f"TOTAL A RECUPERAR: {total}\n") # Total contemplando todos los productos
        #Cuando termina el bloque with el archivo se cierra automaticamente.
        print(f"Reporte generado correctamente en {nombreArchivo}.")

