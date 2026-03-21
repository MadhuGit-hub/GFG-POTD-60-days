class Solution:
    def countBSTs(self, arr):
        n = len(arr)
        
        sorted_arr = sorted(arr)
        
        # Catalan numbers
        dp = [1] * (n + 1)
        
        for i in range(2, n + 1):
            dp[i] = 0
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        
        # map value → index in sorted array
        pos = {}
        for i in range(n):
            pos[sorted_arr[i]] = i
        
        ans = []
        
        for x in arr:
            i = pos[x]   # position in sorted array
            ans.append(dp[i] * dp[n - i - 1])
        
        return ans