class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1, 0], [0, 1], [0,-1]]
        visited = set()
        max_size = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0

            if (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            total = 1
            for dr, dc in directions:
                total += dfs(r + dr, c + dc)

            return total


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_size = max(max_size, dfs(r, c))


        return max_size
