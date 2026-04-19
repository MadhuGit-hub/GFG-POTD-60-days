class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        if len(s1) != len(s2):
            return False
        map1 = {}
        map2 = {}
        
        for i in range(len(s1)):
            c1 = s1[i]
            c2 = s2[i]
            
            if c1 in map1:
                if map1[c1] != c2:
                    return False
            else:
                map1[c1] = c2
            
            if c2 in map2:
                if map2[c2] != c1:
                    return False
            else:
                map2[c2] = c1
        return True