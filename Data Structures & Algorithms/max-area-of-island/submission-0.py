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
                    #if in range rows
                    #if in range cols
                    #if not in seen
                    #if equals to 1
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and
                        (nr,nc) not in seen and 
                        grid[nr][nc] == 1):
                            # add 1 to max area
                            # add to the queue
                            area += 1
                            seen.add((nr,nc))
                            queue.append((nr,nc))
            return area

                        

        #do iteration of the rows and cols
        #if its equal to 1 do the dfs
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in seen:
                    maxArea = max(maxArea, dfs((r,c), 1))

        return maxArea