# This class represents a directed graph using adjacency  
# list representation  
class Graph:  
    def __init__(self, V): # Constructor  
        self.V = V        # No. of vertices  
        self.adj  = [ [] for i in range(V) ]  # adjacency lists  
  
    def add_edge(self,v, w):     # to add an edge to graph 
        self.adj[v].append(w)    # Add w to v’s list.  
        self.adj[w].append(v)    # Add v to w’s list.  

    def print_graph(self):
        print (self.adj)
        for i in self.adj:
            print(i)

# Driver code
if __name__ == "__main__": 
    V = 5
    graph = Graph(V) 
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4) 
  
    graph.print_graph() 