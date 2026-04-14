class Solution:
    def removeSpaces(self, s):
        # code here
        k = []
        k = s.split(" ")
        s = "".join(x for x in k)
        return s
        
        
        """or """
        return s.replace(" ","")
        