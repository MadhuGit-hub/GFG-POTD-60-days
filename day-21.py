class Solution:
    def sumSubMins(self, arr):
        stack = []
        total = 0
        mod = 10**9 + 7
        
        arr = [0] + arr + [0]
        
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                mid = stack.pop()
                left = stack[-1]
                right = i
                
                count = (mid - left) * (right - mid)
                total += arr[mid] * count
            
            stack.append(i)
        
        return total % mod