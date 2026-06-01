from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #gather all the treasure chests
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row,col))

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        #do bfs from those treasure chests
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for ir, ic in directions:
                    nr = r + ir
                    nc = c + ic

                    #if we are in bounds and its not water
                    if (
                        nr in range(ROWS) and
                        nc in range(COLS) and 
                        grid[nr][nc] == 2147483647
                    ):
                        grid[nr][nc] = grid[r][c]+1
                        queue.append((nr,nc))
                    
