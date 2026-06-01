from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()
        fresh = 0
        minutes = 0

        # Add all rotten oranges to queue first
        # Count fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # BFS level by level
        while queue and fresh > 0:
            # everything currently in the queue rots neighbors this minute
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for ir, ic in directions:
                    nr = r + ir
                    nc = c + ic
                    if (
                        nr in range(ROWS)
                        and nc in range(COLS)
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1