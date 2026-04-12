class Solution:
    def isToeplitz(self, mat):
        
        col = len(mat[0])
        ro = len(mat)
        for i in range(1,ro):
            for j in range(1, col):
                if mat[i][j] != mat[i-1][j-1]:
                    return False
        return True
        
        
