from hashTableInt import clientes
from hashTableStr import libros
from graph import ciudad

class Pedido:
    def __init__(self, nombre_libro, id_cliente, destino, estado):
        #if libros.find(libro):
        self.libro = libros.find(nombre_libro)
        #if destino > ciudad.numNodes:
        self.cliente = clientes.find(id_cliente)
        self.destino = destino
        self.estado = estado
        self.tiempo = ciudad.reconstructPath(destino) * 5 