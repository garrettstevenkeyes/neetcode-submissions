from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIslandArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def bfs(cell, total):
            #create queue and add to it
            queue = deque()
            queue.append(cell)
            seen.add(cell)
            total = 1
            #iterate queue
            while queue:
                #remove from queue
                r, c = queue.popleft()
                #check directions
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1 and (nr,nc) not in seen:
                        seen.add((nr, nc))
                        queue.append((nr, nc))
                        total += 1
            
            return total

        #iterate
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]==1 and (row, col) not in seen:
                    res = bfs((row,col),1)
                    maxIslandArea = max(maxIslandArea, res)
                

        return maxIslandArea                 

        
