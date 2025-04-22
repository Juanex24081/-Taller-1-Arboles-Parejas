class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._insertar_recursivo(self.raiz, nuevo)

    def _insertar_recursivo(self, actual, nuevo):
        direccion = input(f"¿Dónde insertar el nodo '{nuevo.valor}' respecto a '{actual.valor}'? (i/d): ")
        if direccion.lower() == 'i':
            if actual.izq is None:
                actual.izq = nuevo
            else:
                self._insertar_recursivo(actual.izq, nuevo)
        elif direccion.lower() == 'd':
            if actual.der is None:
                actual.der = nuevo
            else:
                self._insertar_recursivo(actual.der, nuevo)
        else:
            print("Opción inválida. Usa 'i' para izquierda o 'd' para derecha.")
            self._insertar_recursivo(actual, nuevo)

    def peso(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.peso(nodo.izq) + self.peso(nodo.der)

    def orden(self, nodo):
        if nodo is None:
            return 0
        if nodo.izq is None and nodo.der is None:
            return 1
        return self.orden(nodo.izq) + self.orden(nodo.der)

    def altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

# ---------- Ejecutar ---------
if __name__ == "__main__":
    arbol = ArbolBinario()
    n = int(input("¿Cuántos nodos quieres ingresar?: "))
    for i in range(n):
        valor = input(f"Ingrese el valor para el nodo {i + 1}: ")
        arbol.insertar(valor)

    print("\nResultados:")
    print("Peso del árbol:", arbol.peso(arbol.raiz))
    print("Orden del árbol (número de hojas):", arbol.orden(arbol.raiz))
    print("Altura del árbol:", arbol.altura(arbol.raiz))
