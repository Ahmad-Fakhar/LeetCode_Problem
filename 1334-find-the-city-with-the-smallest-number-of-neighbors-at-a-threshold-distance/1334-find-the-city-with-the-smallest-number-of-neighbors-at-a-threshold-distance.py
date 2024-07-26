class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Step 1: Initialize the distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        # Step 2: Fill the distance matrix with given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Step 3: Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Step 4: Count reachable cities for each city
        reachable_count = []
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1
            reachable_count.append((count, i))
        
        # Step 5: Determine the result
        # Sort by reachable count (ascending) and then by city number (descending)
        reachable_count.sort(key=lambda x: (x[0], -x[1]))
        
        # Return the city with the smallest number of reachable cities and greatest city number in case of tie
        return reachable_count[0][1]