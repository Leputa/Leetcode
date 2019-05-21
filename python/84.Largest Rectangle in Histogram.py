from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        max_area = 0
        i = 0
        while(i < len(heights)):
            # print(stack, max_area)
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


if __name__ == "__main__":
    print(Solution().largestRectangleArea([2,1,5,6,2,3]))