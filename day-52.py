class Solution:
    def countIncreasing(self, arr):
        count = 0
        streak = 0
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                streak += 1
                count += streak
            else:
                streak = 0
                
        return count