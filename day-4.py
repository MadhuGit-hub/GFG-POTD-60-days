class Solution:
    def subarrayXor(self, arr, k):
        # code here
        
        # count no of subarrays
        count = 0
        prexor = 0
        freq = {}
        for i in arr:# each iteration in a list of elements 
            prexor = prexor^i
            if prexor == k:
                count+=1
            
            if prexor^k in freq:
                count += freq[prexor^k]
            freq[prexor] = freq.get(prexor, 0) + 1
        return count
                    