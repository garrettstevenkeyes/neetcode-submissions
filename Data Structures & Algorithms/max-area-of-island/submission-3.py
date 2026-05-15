class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #init the row and col counts
        #create a visited set
        #init a maxarea of 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        #dfs(starting coords, landCount)
        def dfs(start, landCount):
            #create a queue
            queue = collections.deque()
            #get the start r , c coords
            queue.append(start)
            #add to seen
            visited.add(start)
            
            #while queue exists
            while queue:
                #remove from the right
                r, c = queue.pop()

                #check all four directions
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                #iterate over directions
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    #if the row is in bounds
                    #if the col is in bounds
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and
                        #if the space is equal to 1
                        grid[nr][nc] == 1 and
                        #if its not in the seen set
                        (nr,nc) not in visited):
                            #increment area 
                            landCount += 1
                            #add to seen
                            visited.add((nr,nc))
                            #add to queue   
                            queue.append((nr,nc))
            return landCount


        #iteratre over the row and col
        for r in range(ROWS):
            for c in range(COLS):
                #if it equal to 1 its land
                if grid[r][c] == 1 and (r,c) not in visited:
                    #take the max of the max
                    #and the dfs from that spot
                    maxArea = max(maxArea, dfs((r,c),1))

        return maxArea
                