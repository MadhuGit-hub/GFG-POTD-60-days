class Solution:
    def countSquare(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        # prefix sum matrix
        pre = [[0]*(m+1) for _ in range(n+1)]
        
        # build prefix
        for i in range(1, n+1):
            for j in range(1, m+1):
                pre[i][j] = (
                    mat[i-1][j-1]
                    + pre[i-1][j]
                    + pre[i][j-1]
                    - pre[i-1][j-1]
                )
        
        count = 0
        
        # try all squares
        for i in range(n):
            for j in range(m):
                size = 1
                while i + size <= n and j + size <= m:
                    r = i + size
                    c = j + size
                    
                    # sum of square
                    total = (
                        pre[r][c]
                        - pre[i][c]
                        - pre[r][j]
                        + pre[i][j]
                    )
                    
                    if total == x:
                        count += 1
                    
                    size += 1
        
        return count