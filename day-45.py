class Solution:
    def graycode(self,n):
        if n<=0:
            return []
        arr = ["0","1"]
        for i in range(1,n):
            temp = []
            for k in arr:
                temp.append("0" + k)
            for k in arr[::-1]:
                temp.append("1" + k)
            arr = temp
        return arr