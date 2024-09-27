from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        provinces = 0
        visited = [0] * cities

        def bfs(city):
            queue = deque([city])
            visited[city] = 1

            while queue:
                current_city = queue.popleft()
                
                for neighbor, connected in enumerate(isConnected[current_city]):
                    if visited[neighbor] == 0 and connected == 1:
                        queue.append(neighbor)
                        visited[neighbor] = 1

        for city in range(cities):
            if visited[city] == 0:
                bfs(city)
                provinces += 1

        return provinces
