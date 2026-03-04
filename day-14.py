class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        
        # Step 1: XOR of first window
        curr_xor = 0
        for i in range(k):
            curr_xor ^= arr[i]
        
        max_xor = curr_xor
        
        # Step 2: Slide the window
        for i in range(k, n):
            curr_xor ^= arr[i - k]   # remove left element
            curr_xor ^= arr[i]       # add new element
            
            max_xor = max(max_xor, curr_xor)
        
        return max_xor