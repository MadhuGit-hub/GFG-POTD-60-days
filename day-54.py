class Solution:
    def nextPalindrome(self, num):
        n = len(num)

        # take first half
        k = num[:(n+1)//2]

        # mirror
        if n % 2 == 0:
            pal = k + k[::-1]
        else:
            pal = k + k[:-1][::-1]

        # if already greater, return
        if pal > num:
            return pal

        # increase middle
        i = len(k) - 1
        while i >= 0 and k[i] == 9:
            k[i] = 0
            i -= 1

        if i >= 0:
            k[i] += 1
        else:
            return [1] + [0]*(n-1) + [1]

        # mirror again
        if n % 2 == 0:
            return k + k[::-1]
        else:
            return k + k[:-1][::-1]