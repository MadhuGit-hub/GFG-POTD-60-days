from collections import deque

class Solution:
    def minTime(self, root, target):
        
        parent = {}
        target_node = None
        
        # Step 1: Build parent map and find target node
        def dfs(node, par):
            nonlocal target_node
            
            if not node:
                return
            
            parent[node] = par
            
            if node.data == target:
                target_node = node
                
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        
        # Step 2: BFS from target node
        q = deque([target_node])
        visited = set([target_node])
        
        time = 0
        
        while q:
            size = len(q)
            burned = False
            
            for _ in range(size):
                node = q.popleft()
                
                for neigh in (node.left, node.right, parent[node]):
                    if neigh and neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)
                        burned = True
            
            if burned:
                time += 1
        
        return time