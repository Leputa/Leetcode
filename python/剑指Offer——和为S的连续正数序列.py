# -*- coding:utf-8 -*-
import copy

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        tmpList, head, tail = [1, 2], 1, 2
        tmpSum = 3

        while (head < tsum//2 + 1):
            if tmpSum == tsum:
                res.append(copy.deepcopy(tmpList))
                tmpList.pop(0)
                tmpSum -= head
                head += 1
            elif tmpSum < tsum:
                tail += 1
                tmpSum += tail
                tmpList.append(tail)
            else:
                tmpList.pop(0)
                tmpSum -= head
                head += 1
        return res

print(Solution().FindContinuousSequence(3))

