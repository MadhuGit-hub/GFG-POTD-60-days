class Solution:
    def intersection(self,a, b):
        unique = set()
        k = []
        b = set(b)
        for i in a:
            if (i in b) and (i not in unique):
                unique.add(i)
                k.append(i)
        return k