class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        
        left = [0]*n
        right = [0]*n
        
        left[0] = arr[0]
        for i in range(1, n):
            left[i] = min(left[i-1], arr[i])
        
        right[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], arr[i])
        
        for i in range(1, n-1):
            if left[i] < arr[i] < right[i]:
                return [left[i], arr[i], right[i]]
        
        return []