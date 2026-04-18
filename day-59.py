class Solution:
    def maxOnes(self, arr):
        
        c = sum(arr)
        for i in range(len(arr)):
            if arr[i] == 1:
                arr[i] = -1
            else:
                arr[i] = 1
        curr = 0
        maxx = 0
        for i in arr:
            curr = curr + i
            if curr < 0:
                curr = 0
            maxx = max(maxx,curr)
        return maxx + c