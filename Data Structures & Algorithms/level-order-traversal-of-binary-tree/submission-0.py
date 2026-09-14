# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, node, d):
        if not node:
            return
        if d == len(self.ans):
            self.ans.append([])
        self.ans[d].append(node.val)
        self.bfs(node.left, d + 1)
        self.bfs(node.right, d + 1)


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs
        self.depth = 0
        self.ans = []
        self.bfs(root, 0)

        return self.ans

