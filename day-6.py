class Solution:
    def equalSumSpan(self, a1, a2):
        n = len(a1)
        
        # Step 1: create diff array
        diff = [a1[i] - a2[i] for i in range(n)]
        
        prefix_sum = 0
        max_len = 0
        first_occurrence = {}
        
        # Step 2: traverse diff array
        for i in range(n):
            prefix_sum += diff[i]
            
            # Case 1: if prefix_sum becomes 0
            if prefix_sum == 0:
                max_len = i + 1
            
            # Case 2: if prefix_sum seen before
            if prefix_sum in first_occurrence:
                length = i - first_occurrence[prefix_sum]
                max_len = max(max_len, length)
            else:
                # store first occurrence
                first_occurrence[prefix_sum] = i
        
        return max_len