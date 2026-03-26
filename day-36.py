import heapq

class Solution:
    def countPaths(self, V, edges):
        MOD = 10**9 + 7
        
        # Build graph
        graph = [[] for _ in range(V)]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        # Dijkstra setup
        dist = [float('inf')] * V
        ways = [0] * V
        
        dist[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]  # (time, node)
        
        while pq:
            time, node = heapq.heappop(pq)
            
            if time > dist[node]:
                continue
            
            for nei, wt in graph[node]:
                new_time = time + wt
                
                # Found shorter path
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (new_time, nei))
                
                # Found another shortest path
                elif new_time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        
        return ways[V - 1]