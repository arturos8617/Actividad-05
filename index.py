from particula import Particula


class Nodo():
    dato = None
    siguiente = None
    anterior = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Lista_ligada():
    nodo_inicial = None
    nodo_final = None
    no_elements = 0

    def __init__(self):
        self.nodo_inicial = None
        self.nodo_final = None

    def agregar_inicio(self, nodo):
        if(self.no_elements == 0):
            self.nodo_inicial = nodo
            self.nodo_final = nodo
            self.no_elements = self.no_elements + 1
        else:
            temporal = self.nodo_inicial
            temporal.anterior = nodo
            nodo.siguiente = temporal
            self.nodo_inicial = nodo
            self.no_elements = self.no_elements + 1

    def agregar_final(self, nodo):
        if(self.no_elements == 0):
            self.nodo_inicial = nodo
            self.nodo_final = nodo
            self.no_elements = self.no_elements + 1
        else:
            temporal = self.nodo_final
            temporal.siguiente = nodo
            nodo.anterior = temporal
            self.nodo_final = nodo
            self.no_elements = self.no_elements+1

    def mostrar(self):
        temp = self.nodo_inicial
        while(temp):
            print(temp.dato)
            temp = temp.siguiente


lista_ligada = Lista_ligada()

particula1 = Particula(1, 1, 21, 5, 6, 8, 3, 54, 3)
particula2 = Particula(2, 5, 4, 2, 7, 8, 3, 54, 3)
particula3 = Particula(3, 15, 7, 18, 12, 8, 3, 54, 3)
particula4 = Particula(4, 5, 4, 2, 7, 8, 3, 54, 3)

nodo1 = Nodo(particula1)
nodo2 = Nodo(particula2)
nodo3 = Nodo(particula3)
nodo4 = Nodo(particula4)


lista_ligada.agregar_final(nodo1)
lista_ligada.agregar_final(nodo2)
lista_ligada.agregar_inicio(nodo3)
lista_ligada.agregar_final(nodo4)

lista_ligada.mostrar()
