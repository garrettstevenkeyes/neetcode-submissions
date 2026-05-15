class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #define the universe of rows and cols
        ROWS, COLS = len(grid), len(grid[0])
        #init max area var
        maxArea = 0
        #init seen set
        seen = set()
        
        #dfs(node, maxArea)
        def dfs(start, area):
            #init queue
            # add node to queue
            queue = collections.deque()
            queue.append(start)
            seen.add(start)

            #while there are nodes in the queue
            while queue:
                r,c = queue.pop()
        
                #pop the node and save dr, dc vars
                #define the four directions
                # up down left right
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                #iterate over directions
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    #if new row in range rows
                    #if new col in range cols
                    #if (new row, new col) not in seen
                    #if matrix at new row new col equals to 1
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and
                        (nr,nc) not in seen and 
                        grid[nr][nc] == 1):
                            # add 1 to max area
                            #because its increased
                            area += 1
                            #add new row and new column to seen
                            seen.add((nr,nc))
                            # add to the queue
                            queue.append((nr,nc))
            return area

                        

        #do iteration of the rows and cols
        #if its equal to 1 do the dfs
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in seen:
                    maxArea = max(maxArea, dfs((r,c), 1))

        return maxArea