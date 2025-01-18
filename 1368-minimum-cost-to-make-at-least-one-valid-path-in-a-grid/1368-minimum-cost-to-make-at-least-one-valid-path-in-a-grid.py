from typing import List
import heapq
import sys

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # right, left, down, up
        m, n = len(grid), len(grid[0])
        pq = []  # Priority queue to simulate Dijkstra's algorithm
        result = [[sys.maxsize] * n for _ in range(m)]  # Minimum cost to reach each cell

        # Start from the top-left cell
        heapq.heappush(pq, (0, 0, 0))  # (cost, row, col)
        result[0][0] = 0

        while pq:
            curr_cost, i, j = heapq.heappop(pq)

            # If we've already found a cheaper way to this cell, skip processing
            if result[i][j] < curr_cost:
                continue

            # Explore all directions
            for dir_idx in range(4):
                ni, nj = i + directions[dir_idx][0], j + directions[dir_idx][1]

                # Check if the new position is within bounds
                if 0 <= ni < m and 0 <= nj < n:
                    # Check the direction of the current cell
                    grid_dir = grid[i][j] - 1  # 1-indexed to 0-indexed
                    dir_cost = 1 if grid_dir != dir_idx else 0

                    # Calculate the cost to reach the new cell
                    new_cost = curr_cost + dir_cost

                    # If this new cost is cheaper, update and push to the priority queue
                    if new_cost < result[ni][nj]:
                        result[ni][nj] = new_cost
                        heapq.heappush(pq, (new_cost, ni, nj))

        # Return the minimum cost to reach the bottom-right cell
        return result[m - 1][n - 1]
