from PriorityQueue import PriorityQueue

class Libro:
    def __init__(self, nombre, autor, year, genero, cantidad):
        self.nombre = nombre
        self.autor = autor
        self.year = year
        self.genero = genero
        self.cantidad = cantidad  
        self.fila = PriorityQueue()

    def atender_fila(self):
        if not self.fila.isEmpty():
            for i in range(self.cantidad):
                try:                    
                    mayor = self.fila.extractMax()
                    mayor.estado = "Entregado"
                    return mayor                    
                except:
                    pass