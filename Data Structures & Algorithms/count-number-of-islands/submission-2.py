from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        #init rows and cols
        ROWS, COLS = len(grid), len(grid[0])
        #init res
        islands = 0
        #init seen set
        seen = set()
        
        #define bfs
        def bfs(row,col):
            #define queue
            queue = deque()
            #add to queue
            queue.append((row,col))
            #add to seen
            seen.add((row,col))

            #while queue
            while queue:
                #get the top item
                r, c = queue.popleft()
                #check all the directions
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    
                    nr, nc = dr + r, dc + c
                    # if row in the range
                    #if the cols in the range
                    if (nr in range(ROWS) and
                        nc in range(COLS) and
                        #and we havnt seen it
                        (nr, nc) not in seen and
                        #and it is land
                        grid[nr][nc] == "1"):
                            # add to seen spaces and queue
                            seen.add((nr, nc))
                            queue.append((nr,nc))

        #iterate through the grid
        for row in range(ROWS):
            for col in range(COLS):
                #if it equals 1
                if grid[row][col] == "1" and (row, col) not in seen:
                    #do bfs on the grid 
                    bfs(row, col)
                    islands += 1

        return islands
        
