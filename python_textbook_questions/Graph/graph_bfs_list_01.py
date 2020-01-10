
# A class to represent the adjacency list of the node 
class AdjNode: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class Graph: 
    def __init__(self, numv): 
        self.numv = numv 
        self.graph = [None] * self.numv 
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest): 
        # Adding the node to the source node 
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        self.graph[src] = node 
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = AdjNode(src) 
        node.next = self.graph[dest] 
        self.graph[dest] = node 
  
    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.numv): 
            print("Adjacency list of vertex # {}\n head".format(i), end="") 
            curr = self.graph[i] 
            while curr:
                print(" -> {}".format(curr.data), end="") 
                curr = curr.next
            print(" \n") 

def bfs_list(graph, vertex):
    visited = set()
    queue = [vertex] #vertex is node no.
    print("BFS traversal:")
    while queue:
        v = queue.pop(0) #dequeue
        if v == None or v in visited:
            continue
        curr = graph[v] #point to 1st neighbour of vertex id
        print("Vertex #", v)
        visited.add( v )

        while curr:
            if curr.data in visited:
                # print("visited: ", curr.data)
                curr = curr.next
                continue #skip adding this vertex
            #else
            queue.append(curr.data)
            curr = curr.next
        

# Driver code
if __name__ == "__main__": 
    V = 5
    gr = Graph(V) 
    gr.add_edge(0, 1) 
    gr.add_edge(0, 4) 
    gr.add_edge(1, 2) 
    gr.add_edge(1, 3) 
    gr.add_edge(1, 4) 
    gr.add_edge(2, 3) 
    gr.add_edge(3, 4) 
    gr.print_graph() 
    bfs_list(gr.graph, 0)