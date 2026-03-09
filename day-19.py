class Solution:
    def largestSwap(self, s):
        arr = list(s)
        n = len(arr)

        # store last occurrence of each character
        last = {arr[i]: i for i in range(n)}

        for i in range(n):
            # check for larger characters
            for ch in range(9, -1, -1):
                ch = str(ch)
                if ch > arr[i] and ch in last and last[ch] > i:
                    j = last[ch]
                    arr[i], arr[j] = arr[j], arr[i]
                    return "".join(arr)

        return s