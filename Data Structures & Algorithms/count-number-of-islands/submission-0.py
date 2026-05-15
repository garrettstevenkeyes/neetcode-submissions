class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #if there is an empty grid there are no islands
        #so we return 0
        if not grid:
            return 0
        
        #get grid dimensions
        rows, cols = len(grid), len(grid[0])
        #mark grid positions visited
        visited = set()
        #count island numbers
        islands = 0

        def bfs(r,c):
            queue = collections.deque()
            visited.add((r,c))
            queue.append((r,c))

            while queue:
                #get row and col by popping left
                #to make this dfs we can just pop
                row, col = queue.popleft()
                #get all the directions you can move
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                #for each direction
                for dr,dc in directions:
                    #get the new row and col values of where to look
                    r, c = row + dr, col + dc
                    #if the row is in the grid
                    if (r in range(rows) and 
                        #if the col is in the grid
                        c in range(cols) and
                        #if the space is land
                        grid[r][c] == '1' and
                        #if it has not been seen before
                        (r,c) not in visited):
                            #add to the queue
                            queue.append((r,c))
                            #and add to visited
                            visited.add((r,c))

        #iterate through the grid
        for r in range(rows):
            for c in range(cols):
                #if we hit land and we havnt seen it before
                if grid[r][c] == '1' and (r,c) not in visited:
                    #do bfs to visit the island
                    bfs(r, c)
                    islands += 1
        return islands