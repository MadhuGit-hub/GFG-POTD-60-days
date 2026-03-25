class Solution:
    def minHeightRoot(self, V, edges):
        # Edge case
        if V == 1:
            return [0]

        # Build adjacency list
        graph = [set() for _ in range(V)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Find initial leaves
        leaves = deque()
        for i in range(V):
            if len(graph[i]) == 1:
                leaves.append(i)

        remaining = V

        # Trim leaves layer by layer
        while remaining > 2:
            size = len(leaves)
            remaining -= size

            for _ in range(size):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)