from typing import List

class Solution:
    def __init__(self):
        self.cnt = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        tags = [len(grid[0]) * [False] for i in range(len(grid))]
        pos = (0, 0)
        sum_zero = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    tags[i][j] = True
                    pos = (i, j)
                if grid[i][j] == 0:
                    sum_zero += 1
        path_set = set()
        self.traceback(grid, tags, pos, 0, sum_zero)

        return self.cnt

    def traceback(self, grid, tags, pos, cnt, sum_zero):
        row, col = pos
        if grid[row][col] == 2 and cnt == sum_zero + 1:
            self.cnt += 1
            return

        if row >= 1 and grid[row-1][col] != -1 and tags[row-1][col] == False: #up
            tags[row-1][col] = True
            self.traceback(grid, tags, (row-1, col), cnt+1, sum_zero)
            tags[row-1][col] = False
        if row < len(grid) - 1 and grid[row+1][col] != -1 and tags[row+1][col] == False: #down
            tags[row+1][col] = True
            self.traceback(grid, tags, (row+1, col), cnt+1, sum_zero)
            tags[row+1][col] = False
        if col >= 1 and grid[row][col-1] != -1 and tags[row][col-1] == False: #left
            tags[row][col-1] = True
            self.traceback(grid, tags, (row, col-1), cnt+1, sum_zero)
            tags[row][col-1] = False
        if col < len(grid[0]) - 1 and grid[row][col+1] != -1 and tags[row][col+1] == False: #right
            tags[row][col+1] = True
            self.traceback(grid, tags, (row, col+1), cnt+1, sum_zero)
            tags[row][col+1] = False
            




if __name__ == "__main__":
    print(Solution().uniquePathsIII([[1,0,0,0],
                                     [0,0,0,0],
                                     [0,0,2,-1]]))