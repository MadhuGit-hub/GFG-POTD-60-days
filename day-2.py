class Solution:

	def findLargest(self, arr):
	    # code here
	    arr = list(map(str, arr))
        
        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1   # a should come first
            elif a + b < b + a:
                return 1    # b should come first
            else:
                return 0
        
        # Sort using custom comparator
        arr.sort(key=cmp_to_key(compare))
        
        # Join result
        result = ''.join(arr)
        
        # Handle case like [0,0]
        if result[0] == '0':
            return "0"
        
        return result
	         