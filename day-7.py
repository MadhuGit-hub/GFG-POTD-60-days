class Solution:
    def longestSubarray(self, arr, k):
        
        prefix = 0
        first_index = {}
        max_len = 0
        
        for i in range(len(arr)):
            
            # convert to +1 or -1
            if arr[i] > k:
                prefix += 1
            else:
                prefix -= 1
            
            # if prefix > 0, whole subarray valid
            if prefix > 0:
                max_len = i + 1
            
            # store first occurrence
            if prefix not in first_index:
                first_index[prefix] = i
            
            # check prefix-1
            if (prefix - 1) in first_index:
                length = i - first_index[prefix - 1]
                max_len = max(max_len, length)
        
        return max_len