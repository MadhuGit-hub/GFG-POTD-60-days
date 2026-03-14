class Solution:
    def topView(self, root):
        mp = {}

        def dfs(node, hd, level):
            if not node:
                return
            
            if hd not in mp or level < mp[hd][1]:
                mp[hd] = (node.data, level)

            dfs(node.left, hd - 1, level + 1)
            dfs(node.right, hd + 1, level + 1)

        dfs(root, 0, 0)

        ans = []
        for k in sorted(mp):
            ans.append(mp[k][0])

        return ans