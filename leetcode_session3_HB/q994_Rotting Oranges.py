class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        #0 no orange
        #1 orange, 2: rotten
        queue = []
        minute = 0
        ans = 0
        fresh_cnt = 0
        
        #loop through each point in grid and check for rotten oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    #rotten
                    queue.append( [0, i, j] )
                if grid[i][j] == 1: #fresh oranges
                    fresh_cnt += 1
        
        while queue:
            minute, i, j = queue.pop(0) #dequeue
            
            #check all 4 sides and add oranges to queue
            flag = 0
            
            #check all 4 sides
            for x, y in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and grid[x][y] == 1:
                    #rot the side
                    grid[x][y] = 2 #orange is now rotten
                    fresh_cnt -= 1 #one less fresh orange
                    #add to queue to further check its sides
                    queue.append( [minute+1, x, y] )
                    flag = 1
            
            if flag == 1:
                #made orange rot
                minute += 1
            
            ans = max(ans, minute)
        
        
        if fresh_cnt != 0:
            return -1
        else:
            return ans
        