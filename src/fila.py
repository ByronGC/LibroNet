from doubleLinkedList import DoubleLinkedList


class Queue:
    def __init__(self):
        self.items = DoubleLinkedList()
        
    def enqueue(self, item):
        self.items.pushBack(item)
        
    def dequeue(self):
        if self.is_empty():
            print("Error: La cola está vacía")
            return None
        else:
            item = self.items.head.key
            self.items.popFront()
            return item
    
    def peek(self):
        if self.is_empty():
            print("Error: La cola está vacía")
            return None
        else:
            return self.items.head.key
    
    def is_empty(self):
        return self.items.head is None
    
    def make_empty(self):
        self.items.head = None
        self.items.tail = None

    def size(self):
        count = 0
        current = self.items.head
        while current:
            count += 1
            current = current.next
        return count


