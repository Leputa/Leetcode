from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        max_area = 0
        i = 0
        while(i < len(heights)):
            if len(stack) == 0 or heights[i] >= heights[stack[len(stack) - 1]]:
                stack.append(i)
                i += 1
            else:
                idx = stack.pop()
                if len(stack) == 0:
                    max_area = max(max_area, heights[idx] * i)
                else:
                    max_area = max(max_area, heights[idx] * (i - stack[len(stack)-1] - 1))
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        dp = [[0] * len(matrix[0]) for i in range(len(matrix) + 1)]
        
        for j in range(len(matrix[0])):
            for i in range(1, len(matrix) + 1):
                if matrix[i-1][j] == "1":
                    dp[i][j] = dp[i-1][j] + 1

        max_area = 0
        for i in range(1, len(matrix) + 1):
            max_area = max(max_area, self.largestRectangleArea(dp[i]))
        return max_area

if __name__ == "__main__":
    print(Solution().maximalRectangle([
                                      ["1","0","1","0","0"],
                                      ["1","0","1","1","1"],
                                      ["1","1","1","1","1"],
                                      ["1","0","0","1","0"]
                                    ]))


