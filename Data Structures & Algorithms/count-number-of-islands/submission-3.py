from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        #init seen set for grid coordinates
        seen = set()

        def bfs(row,col):
            #init queue with first space
            queue = deque()
            queue.append((row,col))
            #while that queue exists
            while queue:
                #init directions you can go
                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                #pop from the queue
                r,c = queue.popleft()

                #check the directions
                for direction in directions:
                    nr = r + direction[0]
                    nc = c + direction[1]

                    # if the new value is in the grid
                    # and we havnt see it
                    # and its a 1
                    if (nr in range(ROWS)) and (nc in range(COLS)) and (nr,nc) not in seen and grid[nr][nc] == '1':
                        #mark it to seen
                        seen.add((nr,nc))
                        #append to queue
                        queue.append((nr,nc))

        #iterate grid
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                #if its 1 and not in seen
                if (r,c) not in seen and grid[r][c]=='1':
                    #do bfs to capture island
                    bfs(r,c)
                    #increment islands
                    islands += 1
        return islands

