from fila import Queue

class Graph:
    def __init__(self, numNodes, edges):
        self.numNodes = numNodes
        self.data = [[] for i in range(numNodes)]
        self.prev = [None] * len(self.data)
        self.root = 3
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    
    def bfs(self):
        queue = Queue() 
        distance = [None] * len(self.data)
        
        queue.enqueue(self.root)
        distance[self.root] = 0
        
        while not queue.is_empty():
            current = queue.dequeue()
            
            for node in self.data[current]:
                if distance[node] == None:
                    distance[node] = 1+distance[current]
                    self.prev[node] = current
                    queue.enqueue(node)
        
        return queue, distance, self.prev  
    
    def reconstructPath(self, u):
        ct = 0
        self.bfs()
        result = []
        while u != self.root:
            result.append(u)
            u = self.prev[u]
        for i in reversed(result):
            ct += 1
        return ct

numNodes= 10
edges =  [[0,4],[1,4],[4,6],[6,9],[6,5],[5,7],[7,8],[2,5],[3,2],[3,8],[3,1]]
ciudad = Graph(numNodes, edges)