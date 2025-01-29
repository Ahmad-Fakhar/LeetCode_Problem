class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def find_cycle(node, parent):
            if visited[node] == 1:
                visited[parent] = 2
                cycle_nodes.add(node)
                return
            visited[node] = 1
            for neighbor in graph[node]:
                if neighbor != parent:
                    find_cycle(neighbor, node)
                    if node in cycle_nodes:
                        return
            if visited[node] == 2:
                visited[parent] = 2
                cycle_nodes.add(node)    
            return

        graph = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)

        cycle_nodes, visited = set(), [0] * (len(edges)+1)
        find_cycle(1, 0)
        for u, v in reversed(edges):
            if u in cycle_nodes and v in cycle_nodes:
                return [u, v]