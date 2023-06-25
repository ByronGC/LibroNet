from doubleLinkedList import DoubleLinkedList
from claseLibro import Libro
from categorias import categorias

class HashTableStr:
    def __init__(self):
        self.n = 0
        self.a = 34
        self.b = 2
        self.m = 10 
        self.p = 10000019
        self.arr = [None for i in range(self.m)]
        self.arrNuevo = None
    
    def getHash(self, x):
        x = x.lower()
        hash = 0
        s = [ord(letra) for letra in x]
        for i in range(len(x)-1, -1, -1):
            hash += ((hash * 31 + s[i]) % self.p)
        return ((self.a*hash+self.b)%self.p)%self.m
    
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
                    self.add(actual.key.nombre, actual.key.autor, actual.key.year, actual.key.genero, actual.key.cantidad, True)
                    actual = actual.next
            self.arr = self.arrNuevo
            self.arrNuevo = None
    
    def find(self, o):
        L = self.arr[self.getHash(o)]
        if self.arr[self.getHash(o)] == None:
            return False
        actual = self.arr[self.getHash(o)].head
        while actual:
            if actual.key.nombre == o:
                return actual.key
            actual = actual.next
        return False
    
    def add(self, o, autor, año, genero, cantidad, rehash=False):    
        if rehash == False:
            if self.arr[self.getHash(o)] == None:
                self.arr[self.getHash(o)] = DoubleLinkedList()
                self.arr[self.getHash(o)].pushBack(Libro(o, autor, año, genero, cantidad))
                categorias.add(Libro(o, autor, año, genero, cantidad))
                self.n += 1
                self.reHash()
                return
            actual = self.arr[self.getHash(o)].head
            while actual:
                if actual.key == o:
                    self.reHash()
                    return
                actual = actual.next
            self.arr[self.getHash(o)].pushBack(Libro(o, autor, año, genero, cantidad))
            categorias.add(Libro(o, autor, año, genero, cantidad))
            self.n += 1
            self.reHash()
        else:
            if self.arrNuevo[self.getHash(o)] == None:
                self.arrNuevo[self.getHash(o)] = DoubleLinkedList()
                self.arrNuevo[self.getHash(o)].pushBack(Libro(o, autor, año, genero, cantidad))
                categorias.add(Libro(o, autor, año, genero, cantidad))
                self.n += 1
                self.reHash()
                return
            actual = self.arrNuevo[self.getHash(o)].head
            while actual:
                if actual.key == o:
                    self.reHash()
                    return
                actual = actual.next
            self.arrNuevo[self.getHash(o)].pushBack(Libro(o, autor, año, genero, cantidad))
            categorias.add(Libro(o, autor, año, genero, cantidad))
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

libros = HashTableStr()
libros.add("El secreto de Juan", "Juan", 2015, "fantasia", 15)
libros.add("El misterio del espejo", "Ana", 2010, "ciencia ficcion", 8)
libros.add("El jardín de los susurros", "Carlos", 2008, "romance", 10)
libros.add("Versos del corazón", "Laura", 2021, "poesia", 5)
libros.add("El enigma del pasado", "Pedro", 2017, "ficcion", 12)
libros.add("El viaje intergaláctico", "Marta", 2013, "ciencia ficcion", 6)
libros.add("El susurro del viento", "Julia", 2019, "fantasia", 9)
libros.add("El amor prohibido", "Sofia", 2005, "romance", 7)
libros.add("Poesías nocturnas", "Luis", 2018, "poesia", 0)
libros.add("El misterio de la mansión", "Fernando", 2011, "ficcion", 11)
libros.add("El secreto del amanecer", "Elena", 2016, "fantasia", 14)
libros.add("La melodía del corazón", "María", 2009, "romance", 10)
libros.add("Poesías de la naturaleza", "Andrés", 2020, "poesia", 4)
libros.add("El enigma del tiempo", "Gabriel", 2014, "ciencia ficcion", 8)
libros.add("La sombra del pasado", "Luisa", 2007, "ficcion", 12)