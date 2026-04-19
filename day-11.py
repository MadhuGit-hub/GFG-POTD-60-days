class Solution:
    def pushZerosToEnd(self, arr):
        count = 0   # position for next non-zero
        
        # Move non-zero elements forward
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1
        
        # Fill remaining positions with zero
        while count < len(arr):
            arr[count] = 0
            count += 1
        
        return arr