class Solution:
    def canFormPalindrome(self, s):
        s = s.strip()
        unique = {}
        for i in range(len(s)):
            if s[i] not in unique:
                unique[s[i]] = 1
            else:
                unique[s[i]]  =unique.get(s[i])+ 1
        val = list(unique.values())
        k = 0
        for i in val:
            if i%2==0:
                continue
            else:
                k+=1
        if k < 2:
            return True
        else:
            False
