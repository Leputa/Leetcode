class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        top_bottom, left_right = [], []
        len_row, len_col = len(grid), len(grid[0])
        
        for i in range(len_row):
            max_left_right = 0
            for j in range(len_col):
                if grid[i][j] > max_left_right:
                    max_left_right = grid[i][j]
            left_right.append(max_left_right)
        
        for j in range(len_col):
            max_top_bottom = 0
            for i in range(len_row):
                if grid[i][j] > max_top_bottom:
                    max_top_bottom = grid[i][j]
            top_bottom.append(max_top_bottom)

        increase = 0
        for i in range(len_row):
            for j in range(len_col):
                increase += min(left_right[i], top_bottom[j]) - grid[i][j]
        return increase

