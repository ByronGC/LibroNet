from hashTableStr import libros

class Cliente:
    def __init__(self, nombre, id, direccion, telefono):
        self.nombre = nombre
        self.id = id   
        self.direccion = direccion
        self.telefono = telefono  
        self.pedidos = []