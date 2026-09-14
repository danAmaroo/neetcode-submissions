# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, greatest):
        if not node:
            return
        if node.val >= greatest:
            greatest = node.val
            self.goods += 1
        
        self.dfs(node.right, greatest)
        self.dfs(node.left, greatest)


    def goodNodes(self, root: TreeNode) -> int:
        self.goods = 0
        self.dfs(root, root.val)
        return self.goods