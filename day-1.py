class Solution:
    def missingRange(self, arr, low, high):
        arr1 = set(arr)
        list1 = []
        for i in range(low,high+1):
            if i not in arr1:
                list1.append(i)
        return list1