class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            self.components -= 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_union_find = UnionFind(n)
        bob_union_find = UnionFind(n)
        
        used_edges = 0
        
        # Process type 3 edges first
        for edge_type, u, v in edges:
            if edge_type == 3:
                if alice_union_find.union(u - 1, v - 1) | bob_union_find.union(u - 1, v - 1):
                    used_edges += 1
        
        # Process type 1 edges for Alice
        for edge_type, u, v in edges:
            if edge_type == 1:
                if alice_union_find.union(u - 1, v - 1):
                    used_edges += 1
        
        # Process type 2 edges for Bob
        for edge_type, u, v in edges:
            if edge_type == 2:
                if bob_union_find.union(u - 1, v - 1):
                    used_edges += 1
        
        # Check if both Alice and Bob can fully traverse the graph
        if alice_union_find.components != 1 or bob_union_find.components != 1:
            return -1
        
        # Maximum number of edges to remove
        return len(edges) - used_edges
