class Solution:
    def minWindow(self, s, p):
        
        s = s.lower().strip()
        
        if len(p) > len(s):
            return ""
        
        # frequency of characters in p
        fre = {}
        for i in p:
            fre[i] = fre.get(i, 0) + 1
        
        left = 0
        count = 0
        min_len = float('inf')
        start = 0
        
        window = {}
        
        for right in range(len(s)):
            
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            
            if ch in fre and window[ch] <= fre[ch]:
                count += 1
            
            # shrink window
            while count == len(p):
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                
                left_char = s[left]
                window[left_char] -= 1
                
                if left_char in fre and window[left_char] < fre[left_char]:
                    count -= 1
                
                left += 1
        
        if min_len == float('inf'):
            return ""
        
        return s[start:start + min_len]