class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #first if there is no grid return 0
        if not grid: return 0
        #define the universe of rows and cols
        ROWS, COLS = len(grid), len(grid[0])
        #init vars we need which are a seen set, also a counter for island num
        seen = set()
        islands = 0

        #define our bfs, it takes a (r,c) tuple
        def bfs(row,col):
            #init a queue and add to it
            queue = collections.deque()
            queue.append((row,col))
            seen.add((row,col))
            #while we have that queue
            while queue:
                #pop the first element from the left
                #get our r and c values
                r, c = queue.popleft()
                #we need to look in 4 directions, up down left right
                directions = [[0,1],[0,-1],[-1,0],[1,0]]
                #for each of those directions
                for dr,dc in directions:
                    nr, nc = dr + r, dc + c
                    #check if the r is less than the border
                    #check if the c is less than the border
                    #check if the space has been seen already
                    #check if the space is land
                    if (nr in range(ROWS) and
                        nc in range(COLS) and
                        (nr,nc) not in seen and
                        grid[nr][nc] == '1'):
                            #if it is then add it to our seen set
                            seen.add((nr,nc))
                            queue.append((nr,nc))

        #for each r,c value in the grid
        for r in range(ROWS):
            for c in range(COLS):
                #if that r,c is equal to 1 it means we found land
                if grid[r][c] == '1' and (r,c) not in seen:
                    # add that land space to our seen set
                    #do a bfs traversal of the island
                    bfs(r,c)
                    islands += 1
                    
        #return our island counter result
        return islands

