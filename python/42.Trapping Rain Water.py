# class Solution:
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         dic = {}    #高度 =》下标
#         block = 0
#         for i in range(len(height)):
#             h = height[i]
#             for j in range(1, h+1):
#                 pos = dic.get(j, -1)
#                 if pos != -1:
#                     block += (i - pos - 1)
#                 dic[j] = i
#         return block

# if __name__ == '__main__':
# 	print(Solution().trap([1]))
# 上述解法超时

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        max, maxIndex = -1, 0
        for i in range(len(height)):
            if (height[i]) > max:
                max = height[i]
                maxIndex = i

        block = 0
        leftHeight, rightHeight = height[0], height[len(height) -1]

        for i in range(maxIndex):
            if height[i] > leftHeight:
                leftHeight = height[i]
            else:
                block += leftHeight - height[i]

        for i in range(len(height)-1, maxIndex, -1):
            if height[i] > rightHeight:
                rightHeight = height[i]
            else:
                block += rightHeight - height[i]

        return block

if __name__ == "__main__":
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))






