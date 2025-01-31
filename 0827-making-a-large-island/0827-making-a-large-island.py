class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        dir = [(0, 1), (0,-1), (1,0), (-1,0)]

        def dfs(r,c, id):
            if (r <0 or r >=n or c<0 or c >=n or (r,c) in visited or grid[r][c]==0):
                return 0
            visited.add((r,c))
            island = 1
            grid[r][c] = id

            for dx, dy in dir:
                island += dfs(r + dx, c + dy, id)
            return island

        island_map = {}
        uid = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    island_size = dfs(i, j, uid)
                    island_map[uid] = island_size
                    uid += 1

        max_island = max(island_map.values(), default=0)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    adjacent_islands = set()
                    island_size = 1
                    for dx, dy in dir:
                        r, c = i + dx, j + dy
                        if 0 <= r < n and 0 <= c < n and grid[r][c] > 0:
                            adjacent_islands.add(grid[r][c])

                    for island_id in adjacent_islands:
                        island_size += island_map[island_id]
                    max_island = max(max_island, island_size)
        return max_island