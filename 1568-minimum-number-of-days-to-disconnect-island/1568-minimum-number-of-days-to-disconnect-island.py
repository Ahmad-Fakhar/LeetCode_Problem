class Solution:
    def num_islands(self, grid):
        def bfs(i, j):
            queue = deque([(i, j)])
            grid[i][j] = 0
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        queue.append((nx, ny))

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
                    count += 1
        return count

    def minDays(self, grid):
        # Check if the grid is already disconnected
        if self.num_islands([row[:] for row in grid]) != 1:
            return 0

        m, n = len(grid), len(grid[0])

        # Try removing each cell to see if it disconnects the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if self.num_islands([row[:] for row in grid]) != 1:
                        return 1
                    grid[i][j] = 1

        # If no single cell removal works, return 2
        return 2