from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        #count rows and cols
        ROWS, COLS = len(grid), len(grid[0])
        #init seen to not revisit
        seen = set()
        #do a dfs
        def bfs(row,col):
            #init queue
            queue = deque()
            queue.append((row,col))
            #iterate queue
            while queue:
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                r, c = queue.popleft()
                #check all directions
                for direction in directions:
                    nr = r + direction[0]
                    nc = c + direction[1]
                    #is it in the grid, not seen and equal to land
                    #if yes mark it seen and add to queue
                    if (nr in range(ROWS)) and (nc in range(COLS)) and (nr, nc) not in seen and grid[nr][nc]=='1':
                        seen.add((nr,nc))
                        queue.append((nr,nc))
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in seen and grid[r][c]=='1':
                    bfs(r,c)
                    islands += 1
        
        return islands
