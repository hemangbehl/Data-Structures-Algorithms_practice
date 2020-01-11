## matrix representation of a graph
## https://www.programiz.com/dsa/graph-adjacency-matrix

class Graph:
    def __init__(self, numvertex):
        #adjMatrix = adjacency matrix 2D 
        self.adjMatrix = [ [-1] * numvertex for x in range(numvertex) ]
        self.numvertex = numvertex #set size as no. of vertices
 
    def add_edge(self, frm, to, cost = 0): #add_edge src to dest with cost/weight 'x'
        
        if frm == to:
            print("same source and destination. Invalid path.")
            return

        self.adjMatrix[frm][to] = cost
        #for directed graph do not add this
        self.adjMatrix[to][frm] = cost

    def get_edges(self): #edges connections b/w 2 nodes(vertices)
        edges = [] #empty list to store the edges
        # add the edges which are not absent(-1)
        for i in range (self.numvertex):
            for j in range (self.numvertex):
                if (self.adjMatrix[i][j] != -1):
                    edges.append( ( i, j, self.adjMatrix[i][j] ) )
        
        return edges
    
    def printMatrix(self):
        n = self.numvertex
        for i in range(0, n): #for (i = 0; i < n; i++)
            for j in range(0, n): 
                if ( j != n - 1 ):
                    print(self.adjMatrix[i][j], ",", end='')
                else:
                    print(self.adjMatrix[i][j]) #delimeter = /n

def BFS(matrix, vertex):
    queue = [vertex]
    visited = set()
    visited.add(vertex)
    
    while queue:
        curr_i = queue.pop(0) #dequeue
        print("vertex # ", curr_i)

        for j in range(0, len(matrix[0]) ):
            if ( matrix[curr_i][j] != -1 ) and ( j not in visited ):
                queue.append(j)
                visited.add(j)
    



G = Graph(6) #set size as '6'
G.add_edge(0, 5, 10)
G.add_edge(1, 4, 20)
G.add_edge(3, 1, 30)
G.add_edge(2, 5, 40)
G.add_edge(4, 3, 50)
G.add_edge(1, 2, 60)
G.printMatrix()
print("")
BFS( G.adjMatrix, 0 )