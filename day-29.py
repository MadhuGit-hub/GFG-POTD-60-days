class Solution:
    def largestBst(self, root):
        
        self.max_size = 0
        
        def helper(node):
            # Base case
            if not node:
                return (float('inf'), float('-inf'), 0)
            
            left_min, left_max, left_size = helper(node.left)
            right_min, right_max, right_size = helper(node.right)
            
            # Check BST condition
            if left_max < node.data < right_min:
                curr_size = left_size + right_size + 1
                self.max_size = max(self.max_size, curr_size)
                
                return (
                    min(left_min, node.data),
                    max(right_max, node.data),
                    curr_size
                )
            
            # If not BST, return invalid range
            return (float('-inf'), float('inf'), 0)
        
        helper(root)
        return self.max_size