class Solution:
    @staticmethod
    def topological_sort(n: int, conditions: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        for u, v in conditions:
            graph[u].append(v)
            in_degree[v] += 1
            
        queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
        top_order = []
        
        while queue:
            node = queue.popleft()
            top_order.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(top_order) == n:
            return top_order
        return []
    
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_order = Solution.topological_sort(k, rowConditions)
        col_order = Solution.topological_sort(k, colConditions)
        
        if not row_order or not col_order:
            return []
        
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            r = row_pos[num]
            c = col_pos[num]
            matrix[r][c] = num
            
        return matrix