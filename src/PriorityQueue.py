import math
from graph import ciudad

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return math.floor(i/2)
    
    def leftChild(self, i):
        if i == 0:
            return 1
        return 2*i
    
    def rightChild(self, i):
        if i == 0:
            return 2
        return 2*i + 1
    
    def swap(self, i1, i2):
        temp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = temp
    
    def siftUp(self, i):
        while i > 0 and ciudad.reconstructPath(self.heap[self.parent(i)].destino) < ciudad.reconstructPath(self.heap[i].destino):
            self.swap(self.parent(i), i)
            i = self.parent(i)
    
    def siftDown(self, i):
        maxIndex = i
        l = self.leftChild(i)
        if l <= (len(self.heap)-1) and ciudad.reconstructPath(self.heap[l].destino) > ciudad.reconstructPath(self.heap[maxIndex].destino):
            maxIndex = l
        r = self.rightChild(i)
        if r <= (len(self.heap)-1) and ciudad.reconstructPath(self.heap[r].destino) > ciudad.reconstructPath(self.heap[maxIndex].destino):
            maxIndex = r
        if i != maxIndex:
            self.swap(i, maxIndex)
            self.siftDown(maxIndex)
    
    def insert(self, o):
        self.heap.append(o)
        self.siftUp(len(self.heap)-1)
    
    def extractMax(self):
        result = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.siftDown(0)
        self.heap.pop()
        return result
    
    def remove(self, i):
        self.heap[i] = math.inf
        self.siftUp(i)
        self.extractMax()
    
    def changePriority(self, i, p):
        oldp = self.heap[i]
        self.heap[i] = p
        if p > oldp:
            self.siftUp(i)
        else:
            self.siftDown(i)

    def isEmpty(self):
        if len(self.heap) == 0:
            return True 
        else:
            return False

fila = PriorityQueue()