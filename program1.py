class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid or not grid[0]: 
            return 0 
        
        rows,cols = len(grid),len(grid[0]) 
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def dfs(r,c): 
            grid[r][c]='w' 
        
            for dr,dc in directions:  
                nr,nc= r+dr, c+dc    
                if 0<= nr < rows and 0<=nc<cols and grid[nr][nc]=='L': 
                    dfs(nr,nc) 
                    
        num_islands=0  
        
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] =='L': 
                    dfs(r,c) 
                    num_islands +=1  
                                 
        
