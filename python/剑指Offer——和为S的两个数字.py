# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        head = 0
        tail = len(array) - 1
        while head < tail:
            if array[head] + array[tail] == tsum:
                return [array[head], array[tail]]
            elif array[head] + array[tail] < tsum:
                head += 1
            else:
                tail -= 1
        return []