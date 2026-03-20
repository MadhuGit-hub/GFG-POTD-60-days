'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        
        arr = []
        self.inorder(root, arr)
        
        pred = None
        succ = None
        
        for i in range(len(arr)):
            if arr[i].data < key:
                pred = arr[i]
            elif arr[i].data > key and succ is None:
                succ = arr[i]
        
        return pred, succ
    
    
    def inorder(self, root, arr):
        if root is None:
            return
        
        self.inorder(root.left, arr)
        arr.append(root)   
        self.inorder(root.right, arr)