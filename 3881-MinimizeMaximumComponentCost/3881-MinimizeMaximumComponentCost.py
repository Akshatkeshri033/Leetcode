# Last updated: 8/20/2025, 5:48:30 PM
class Solution(object):
    def minCost(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        if k == n:
            return 0  # No edge needed; all components are isolated

        parent = list(range(n))

        def find(u):
            while u != parent[u]:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            parent[pu] = pv
            return True

        edges.sort(key=lambda x: x[2])

        components = n
        max_cost = 0

        for u, v, w in edges:
            if union(u, v):
                max_cost = max(max_cost, w)
                components -= 1
                if components == k:
                    break

        return max_cost
