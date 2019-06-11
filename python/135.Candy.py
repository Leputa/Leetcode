from typing import List

# class Solution:
#     def candy(self, ratings: List[int]) -> int:
'''
该解法有误，但应该存在空间复杂度为O(1)的方法，目前想不出来
头条面试中有过一道成环的题
'''
#         ret = len(ratings)
#         down_length = 0
#         up_length = 0
#         for i in range(1, len(ratings)):
#             if ratings[i] >= ratings[i-1]:
#                 ret += down_length * (down_length + 1) // 2
#                 down_length = 0
#             else:
#                 down_length += 1

#             if ratings[i] <= ratings[i-1]:
#                 ret += up_length * (up_length + 1) // 2
#                 up_length = 0
#             else:
#                 up_length += 1


#         ret += down_length * (down_length + 1) // 2
#         ret += up_length * (up_length + 1) // 2
#         return ret


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1] + 1)
        print(candy)
        return sum(candy)

        
if __name__ == "__main__":
    print(Solution().candy([1,3,4,5,2]))