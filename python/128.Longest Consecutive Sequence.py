import copy

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = dict()
        for num in nums:
            dic[num] = 1

        longest_length = 0
        for key in copy.deepcopy(dic):
            if key in dic:
                length = 1
                num = key + 1
                while num in dic:
                    del dic[num]
                    length += 1
                    num += 1
                num = key - 1
                while num in dic:
                    del dic[num]
                    length += 1
                    num -= 1
                longest_length = max(length, longest_length)

        return longest_length




