class Solution:
    def minCost(self, houses):
        import heapq
        
        n = len(houses)
        visited = [False] * n
        min_heap = [(0, 0)]  # (cost, index)
        total_cost = 0
        
        while min_heap:
            cost, i = heapq.heappop(min_heap)
            
            if visited[i]:
                continue
                
            visited[i] = True
            total_cost += cost
            
            x1, y1 = houses[i]
            
            for j in range(n):
                if not visited[j]:
                    x2, y2 = houses[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, j))
        
        return total_cost