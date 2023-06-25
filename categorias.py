from doubleLinkedList import DoubleLinkedList

class Categorias():
    def __init__(self):
        self.cienciaFiccion = DoubleLinkedList()
        self.fantasia = DoubleLinkedList()
        self.romance = DoubleLinkedList()
        self.poesia = DoubleLinkedList()
        self.ficcion = DoubleLinkedList()
    
    def add(self, libro):
        if libro.genero == "ciencia ficcion":
            self.cienciaFiccion.pushFront(libro.nombre)
        if libro.genero == "fantasia":
            self.fantasia.pushFront(libro.nombre)
        if libro.genero == "romance":
            self.romance.pushFront(libro.nombre)
        if libro.genero == "poesia":
            self.poesia.pushFront(libro.nombre)
        if libro.genero == "ficcion":
            self.ficcion.pushFront(libro.nombre)


categorias = Categorias()