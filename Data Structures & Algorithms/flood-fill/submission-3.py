class Solution:
    def dfs(self, image, r, c, visit, color):
        ROW, COL = len(image), len(image[0])
        if r < 0 or c < 0 or r >= ROW or c >= COL or (r,c) in visit or image[r][c] != self.start:
            return image

        visit.add((r,c))

        image[r][c] = color

        self.dfs(image, r + 1, c, visit, color)
        self.dfs(image, r - 1, c, visit, color)
        self.dfs(image, r, c + 1, visit, color)
        self.dfs(image, r, c - 1, visit, color)

        visit.remove((r,c))

        return image



    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.start = image[sr][sc]
        self.visit = set()
        return self.dfs(image, sr, sc, self.visit, color)
        