class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        #0 no orange
        #1 orange, 2: rotten
        visited = set()
        queue = []
        minute = 0
        ans = 0
        
        #loop through each point in grid and check for rotten oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    #rotten
                    queue.append( [0, i, j] )
        
        while queue:
            pair = queue.pop(0) #dequeue
            minute = pair[0]
            i = pair[1]
            j = pair[2]
            
            #check all 4 sides and add oranges to queue
            minute = self.rot(grid, minute, i, j, queue, visited, ans)
            
            ans = max(ans, minute)
        
        
        #check for remaining fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    #fresh orange detected
                    return -1 
        
        return ans
    
    def rot(self, grid, minute, i, j, queue, visited, ans):
        #rot() is called on verified rotten oranges
        visited.add( (i, j) )
        flag = 0
        
        #check all 4 sides
        for direc in [(0,1),(0,-1),(1,0),(-1,0)]:
            x = i + direc[0]
            y = j + direc[1]
            
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and (x, y) not in visited and grid[x][y] == 1:
                #rot the side
                grid[x][y] = 2
                #add to queue to further check its sides
                queue.append( [minute+1, x, y] )
                flag = 1
        
        if flag == 1:
            #made orange rot
            minute += 1
        
        return minute
        
            