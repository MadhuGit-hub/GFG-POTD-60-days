class Solution:
    def hIndex(self, citations):
        #code here
        citations.sort()
        citations.reverse()
        for i, citation in enumerate(citations):
            if i>=citation:
                return i
        return len(citations)