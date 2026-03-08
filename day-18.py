class Solution:
    def pythagoreanTriplet(self, arr):
        n = len(arr)
        
        # Square all numbers
        sq = [x*x for x in arr]
        
        # Store squares in set
        s = set(sq)
        
        for i in range(n):
            for j in range(i+1, n):
                if sq[i] + sq[j] in s:
                    return True
                    
        return False