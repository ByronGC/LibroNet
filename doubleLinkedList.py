class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def pushBack(self, key):
        node = Node(key)
        if self.tail == None:
            self.head = self.tail = node
            node.prev = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            
    def popBack(self):
        if self.head == None:
            print("Error, lista vacia")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
    def popFront(self):
        if self.head == None:
            print("Error, lista vacia")
        self.head = self.head.next
        if self.head == None:
            self.tail = None
            
    def pushFront(self, key):
        node = Node(key)
        node.next = self.head
        self.head = node
        if self.tail == None:
            self.tail = self.head
            
    def addAfter(self, node1, key):
        node = self.find(node1)
        if node != None:
            node2 = Node(key)
            node2.next = node.next
            node2.prev = node
            node.next = node2
            if node2.next != None:
                node2.next.prev = node2
            if self.tail == node:
                self.tail = node2
        else:
            print("El nodo de referencia no existe")
    
    def find(self,key):
        actual = self.head
        while actual:
            if actual.key == key:
                return actual
            actual = actual.next
        return None
    
    def remove(self, node1):
        node = self.find(node1)
        if node.next == None:
            self.popBack()
            return
        elif node.prev == None:
            self.popFront()
            return
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def print_list(self):
        actual = self.head
        print('[', end='')
        while actual:                        
            if actual.next != None:
                print(actual.key, end=' ')            
                actual = actual.next
            else:
                print(actual.key, end='') 
                actual = actual.next
        print(']')

pedidos = DoubleLinkedList()