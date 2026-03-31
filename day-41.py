class Solution:
    def maxProfit(self, arr, k):
        if not arr:
            return 0
        max_price = 0
        min_price = arr[0]
        for price in arr:
            if price < min_price:
                min_price = price
            elif price > min_price+k:
                max_price = max_price+price-min_price-k
                min_price = price-k 
            
        return max_price