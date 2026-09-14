class Solution:
    def dfs(self, node, d):
        if not node:
            return
        if d > self.depth:
            self.depth = d
            self.ans.append(node.val)

        self.dfs(node.right, d + 1)
        self.dfs(node.left, d + 1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.depth = -1
        self.dfs(root, 0)
        return self.ans