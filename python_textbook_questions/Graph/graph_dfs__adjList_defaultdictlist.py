from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def printAllEdges(self):
        print("all edges:")
        for i in self.graph:
            print("vertex #", i, ": ", end='')
            for j in self.graph[i]:
                print(j, end='-> ')
            print("")

    def DFS(self, v):
        stack = list()
        stack.append(v)
        visited = set()
        visited.add(v)

        while stack:
            v = stack.pop()
            print(v, end=' ')
            
            for w in self.graph[v]:
                if w not in visited:
                    visited.add(w)
                    stack.append(w)
        print("")

#driver code
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(2, 1)
g.add_edge(4, 0)
g.add_edge(3, 4)
g.add_edge(0, 3)
g.add_edge(0, 2)
g.DFS(0)
g.printAllEdges()
