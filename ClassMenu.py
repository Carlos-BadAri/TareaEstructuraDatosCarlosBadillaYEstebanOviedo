from ClassNodoYClassListaDoblementeEnlazada import Nodo, ListaDoblementeEnlazada
from ClassProducto import producto
from ClassReporte import Reporte


def menu(lista):

    reporte = Reporte()

    while True:

        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar productos (recursivo)")
        print("5. Ver frecuencia de productos por pais")
        print("6. Generar reporte de recuperacion (archivo .txt)")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        match opcion:

            case "1":
                agregarProducto(lista)

            case "2":
                eliminarProducto(lista)

            case "3":

                if lista.listaVacia():
                    print("No hay productos registrados.")

                else:

                    Id = int(input("Ingrese el Id del producto a buscar: "))

                    encontrado = lista.buscarIDProducto(Id)

                    if encontrado is not None:

                        print("Producto encontrado:")
                        encontrado.imprimir()

                    else:

                        print(f"No se encontro un producto con Id {Id}.")

            case "4":

                if lista.listaVacia():
                    print("No hay productos registrados.")

                else:

                    print("Lista de productos:")
                    lista.mostrarRecursivo()

            case "5":

                reporte.mostrarFrecuenciaPaises(lista)

            case "6":

                reporte.generarReporteRecuperacion(lista)

            case "7":

                print("Saliendo del programa...")
                break

            case _:

                print("Opcion invalida, intente de nuevo.")


def pedirDatosProducto():

    Id = int(input("Ingrese el Id del producto: "))
    nombre = input("Ingrese el nombre: ")
    precio = float(input("Ingrese el precio: "))
    pais = input("Ingrese el pais: ")
    existencias = int(input("Ingrese las existencias: "))

    return producto(Id, nombre, precio, pais, existencias)


def agregarProducto(lista):

    print("\n¿Dónde desea insertar el producto?")
    print("1. Al inicio")
    print("2. Al final")
    print("3. En una posicion específica")

    subopcion = input("Seleccione una opcion: ")

    match subopcion:

        case "1":

            nuevoProducto = pedirDatosProducto()

            lista.agregarAlInicio(nuevoProducto)

            print("Producto agregado al inicio.")

        case "2":

            nuevoProducto = pedirDatosProducto()

            lista.agregarAlFinal(nuevoProducto)

            print("Producto agregado al final.")

        case "3":

            posicion = int(
                input(f"Ingrese la posicion (0 a {lista.tamano}): "))

            if posicion < 0 or posicion > lista.tamano:

                print("Posicion invalida.")
                return

            nuevoProducto = pedirDatosProducto()

            lista.agregarEnPosicion(
                nuevoProducto,
                posicion
            )

            print(f"Producto agregado en la posicion {posicion}.")

        case _:

            print("Opcion invalida.")


def eliminarProducto(lista):

    if lista.listaVacia():

        print("No hay productos para eliminar.")
        return

    print("\n¿Como desea eliminar el producto?")
    print("1. Por Id")
    print("2. Al inicio")
    print("3. Al final")
    print("4. En una posicion especifica")

    subopcion = input("Seleccione una opcion: ")

    match subopcion:

        case "1":

            Id = int(input("Ingrese el Id del producto a eliminar: "))

            eliminado = lista.eliminarProductoPorID(Id)

            if eliminado is not None:

                print("Producto eliminado:")
                eliminado.imprimir()

            else:

                print(f"No se encontro un producto con Id {Id}.")

        case "2":

            eliminado = lista.eliminarAlInicio()

            print("Producto eliminado:")
            eliminado.imprimir()

        case "3":

            eliminado = lista.eliminarAlFinal()

            print("Producto eliminado:")
            eliminado.imprimir()

        case "4":

            posicion = int(
                input(f"Ingrese la posicion " f"(0 a {lista.tamano - 1}): "))

            if posicion < 0 or posicion > lista.tamano - 1:

                print("Posicion invalida.")
                return

            eliminado = lista.eliminarEnPosicion(posicion)

            print("Producto eliminado:")
            eliminado.imprimir()

        case _:

            print("Opcion invalida.")


if __name__ == "__main__":

    lista = ListaDoblementeEnlazada()
    menu(lista)