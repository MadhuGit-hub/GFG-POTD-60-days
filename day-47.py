import heapq

class Node:
    def __init__(self, freq, char=None, left=None, right=None, index=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.index = index

class Solution:
    def huffmanCodes(self, s, f):
        # Handle edge case: only one character
        if len(s) == 1:
            return ["0"]
        
        heap = []
        
        # Push nodes with (frequency, index, node)
        for i in range(len(s)):
            heapq.heappush(heap, (f[i], i, Node(f[i], s[i], None, None, i)))
        
        # Build Huffman tree
        while len(heap) > 1:
            f1, idx1, left = heapq.heappop(heap)
            f2, idx2, right = heapq.heappop(heap)
            
            # Create new internal node
            newNode = Node(f1 + f2, None, left, right, min(idx1, idx2))
            
            # Push back with (frequency, min_index, node)
            heapq.heappush(heap, (f1 + f2, min(idx1, idx2), newNode))
        
        root = heap[0][2]
        result = []
        
        # Preorder traversal to get codes
        def preorder(node, code):
            if not node:
                return
            # If leaf node (has character), add code to result
            if node.char is not None:
                result.append(code)
            # Traverse left and right
            if node.left:
                preorder(node.left, code + "0")
            if node.right:
                preorder(node.right, code + "1")
        
        preorder(root, "")
        return result