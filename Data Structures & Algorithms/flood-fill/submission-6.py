class Solution:
    def dfs(self, image, r, c, color):
        ROW, COL = len(image), len(image[0])
        if r < 0 or c < 0 or r >= ROW or c >= COL or image[r][c] != self.start:
            return 

        image[r][c] = color

        self.dfs(image, r + 1, c, color)
        self.dfs(image, r - 1, c, color)
        self.dfs(image, r, c + 1,color)
        self.dfs(image, r, c - 1,color)

        return image



    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        self.start = image[sr][sc]
        return self.dfs(image, sr, sc, color)
        