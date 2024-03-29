class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaCircular:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            nuevo_nodo.siguiente = nuevo_nodo  # El nuevo nodo apunta a sí mismo
            self.primero = nuevo_nodo
        else:
            nodo_actual = self.primero
            while nodo_actual.siguiente != self.primero:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.primero

    def imprimir_lista(self):
        if self.esta_vacia():
            print("La lista enlazada circular está vacía.")
            return
        nodo_actual = self.primero
        while True:
            print(nodo_actual.dato, end=" -> ")
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
        print()

# Ejemplo de uso
lista_circular = ListaEnlazadaCircular()
lista_circular.insertar_al_final(1)
lista_circular.insertar_al_final(2)
lista_circular.insertar_al_final(3)

print("Lista enlazada circular:")
lista_circular.imprimir_lista()
