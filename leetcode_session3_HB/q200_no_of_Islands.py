class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0
        
        
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == '1':
                    #atleast a part of an island
                    self.dfsMark0(grid, i, j)
                    cnt += 1
        
        return cnt
    
    def dfsMark0(self, grid, row, col):
        #check if row col is out of bounds
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return
        
        if grid[row][col] != '1':
            return
        
        #make zero
        grid[row][col] = 0
        
        #call dfsMark0 on all 4 sides
        self.dfsMark0(grid, row   , col + 1)
        self.dfsMark0(grid, row   , col - 1)
        self.dfsMark0(grid, row + 1, col   )
        self.dfsMark0(grid, row - 1, col   )