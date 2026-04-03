class Solution:
    def diagView(self, mat):
        if not mat:
            return []
        n = len(mat)
        result = []
        for col in range(n):
            i = 0
            j = col
            while i < n and j >= 0:
                result.append(mat[i][j])
                i += 1
                j -= 1
        for row in range(1, n):
            i = row
            j = n - 1
            while i < n and j >= 0:
                result.append(mat[i][j])
                i += 1
                j -= 1
        
        return result