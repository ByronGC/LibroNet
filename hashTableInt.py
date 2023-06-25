from doubleLinkedList import DoubleLinkedList
from claseCliente import Cliente

class HashTableInt:
    def __init__(self):
        self.n = 0
        self.a = 34
        self.b = 2
        self.m = 10 
        self.p = 10000019
        self.arr = [None for i in range(self.m)]
        self.arrNuevo = None
    
    def getHash(self, x):
        return ((self.a*x+self.b)%self.p)%self.m
    
    def reHash(self):
        if self.n/self.m > 1:
            self.n = 0
            self.arrNuevo = [None for i in range(len(self.arr)*2)]
            self.m = len(self.arrNuevo)
            for i in self.arr:
                if i == None:
                    continue
                actual = i.head
                while actual:
                    self.add(actual.key.nombre, actual.key.id, actual.key.direccion, actual.key.telefono, True)
                    actual = actual.next
            self.arr = self.arrNuevo
            self.arrNuevo = None
    
    def find(self, o):
        L = self.arr[self.getHash(o)]
        if self.arr[self.getHash(o)] == None:
            return False
        actual = self.arr[self.getHash(o)].head
        while actual:
            if actual.key.id == o:
                return actual.key
            actual = actual.next
        return False
    
    def add(self, nombre, o, direccion, telefono, rehash=False):        
        if rehash == False:
            if self.arr[self.getHash(o)] == None:
                self.arr[self.getHash(o)] = DoubleLinkedList()
                self.arr[self.getHash(o)].pushBack(Cliente(nombre, o, direccion, telefono))
                self.n += 1
                self.reHash()
                return
            actual = self.arr[self.getHash(o)].head
            while actual:
                if actual.key == o:
                    self.reHash()
                    return
                actual = actual.next
            self.arr[self.getHash(o)].pushBack(Cliente(nombre, o, direccion, telefono))
            self.n += 1
            self.reHash()
        else:
            if self.arrNuevo[self.getHash(o)] == None:
                self.arrNuevo[self.getHash(o)] = DoubleLinkedList()
                self.arrNuevo[self.getHash(o)].pushBack(Cliente(nombre, o, direccion, telefono))
                self.n += 1
                self.reHash()
                return
            actual = self.arrNuevo[self.getHash(o)].head
            while actual:
                if actual.key == o:
                    self.reHash()
                    return
                actual = actual.next
            self.arrNuevo[self.getHash(o)].pushBack(Cliente(nombre, o, direccion, telefono))
            self.n += 1
            self.reHash()
    
    def printTable(self):
        ct = 0
        for i in self.arr:
            if i == None:
                print("(" + str(ct) + "):", end = '')
                print("[]")
                ct += 1
                continue
            actual = i.head
            print("(" + str(ct) + "):", end = '  ')
            print("[", end = '')
            while actual:
                if actual.next == None:
                    print(actual.key.nombre, end = '')
                else:
                    print(actual.key.nombre, end = ', ')
                actual = actual.next
            ct += 1
            print("]")
    
    def remove(self, o):
        item = self.find(o)
        if not item: 
            return
        self.arr[self.getHash(o)].remove(item)


clientes = HashTableInt()
clientes.add("Juan Pérez", 1234567,1, "3165478569")
clientes.add("María González", 2345678, 2, "3175487963")
clientes.add("Pedro López", 3456789, 3, "3185698745")
clientes.add("Ana Rodríguez", 4567890, 4, "3154879652")
clientes.add("Luisa García", 5678901, 5, "3145687932")
clientes.add("Carlos Martínez", 6789012, 6, "3124578963")
clientes.add("Laura Sánchez", 7890123, 7, "3135698742")
clientes.add("Miguel Torres", 8901234, 8, "3145879652")
clientes.add("Sofía Ramírez", 9012345, 9, "3165487923")
clientes.add("Javier Romero", 1234509, 0, "3175698475")
clientes.add("Ana Martínez", 2345610, 3, "3165487236")
clientes.add("Carlos Rodríguez", 3456711, 5, "3104758962")
clientes.add("María García", 4567812, 2, "3185247693")
clientes.add("Nicolas Rubio", 5678913, 8, "3196874521")
clientes.add("Sofía Fernández", 6789014, 3, "3129876543")