class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        tag = [[0]*len(grid[0]) for i in range(len(grid))]
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and tag[i][j] == 0:
                    area = self.dfs(grid, tag, i, j, 1)
                    if area > max_area:
                        max_area = area
        return max_area

    def dfs(self, grid, tag, i, j, area):
        tag[i][j] = 1
        if i > 0 and grid[i-1][j] == 1 and tag[i-1][j] == 0:
            area = self.dfs(grid, tag, i-1, j, area + 1)
        if i < len(grid)-1 and grid[i+1][j] == 1 and tag[i+1][j] == 0:
            area = self.dfs(grid, tag, i+1, j, area + 1)
        if j > 0 and grid[i][j-1] == 1 and tag[i][j-1] == 0:
            area = self.dfs(grid, tag, i, j-1, area + 1)
        if j < len(grid[0])-1 and grid[i][j+1] == 1 and tag[i][j+1] == 0:
            area = self.dfs(grid, tag, i, j+1, area + 1)
        return area
