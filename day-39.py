class Solution:
    def countPartitions(self, arr, diff):
        s = sum(arr)
        if (s + diff) % 2 != 0:
            return 0
        target = (s + diff) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[target]