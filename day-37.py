class Solution:
    def articulationPoints(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [0]*V
        disc = [0]*V
        low = [0]*V
        parent = [-1]*V
        ap = [0]*V
        time = [0]

        def dfs(u):
            visited[u] = 1
            disc[u] = low[u] = time[0]
            time[0] += 1
            child = 0

            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u
                    child += 1
                    dfs(v)

                    low[u] = min(low[u], low[v])

                    if parent[u] == -1 and child > 1:
                        ap[u] = 1
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = 1

                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])

        for i in range(V):
            if not visited[i]:
                dfs(i)

        ans = [i for i in range(V) if ap[i] == 1]
        return ans if ans else [-1]