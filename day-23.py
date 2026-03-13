class Solution:
    def generateIp(self, s):
        arr = []
        n = len(s)

        if n < 4 or n > 12:
            return [-1]

        def valid(part):
            if len(part) == 0:
                return False
            if len(part) > 1 and part[0] == '0':
                return False
            return 0 <= int(part) <= 255

        for i in range(1,4):
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):

                    if i < n and j < n and k < n:

                        p1 = s[:i]
                        p2 = s[i:j]
                        p3 = s[j:k]
                        p4 = s[k:]

                        if valid(p1) and valid(p2) and valid(p3) and valid(p4):
                            arr.append(p1+"."+p2+"."+p3+"."+p4)

        if len(arr) == 0:
            return [-1]

        return arr