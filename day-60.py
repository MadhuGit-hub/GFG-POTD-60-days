class Solution:
    def isPower(self, x, y):
        if x == 1:
            return False
        while y%x == 0:
            y = y//x
        return y == 1