# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) == 0:
            return False
        
        numbers.sort()
        zero_cnt = 0
        pos = 0
        for i in range(len(numbers)):
            if numbers[i] == 0:
                zero_cnt += 1
            else:
                pos = i
                break

        if len(numbers) - pos == 1:
            return True
        for i in range(pos + 1, len(numbers)):
            if numbers[i] == numbers[i-1]:
                return False
            if numbers[i] - numbers[i-1]!=1:
                zero_cnt -= (numbers[i]-numbers[i-1]-1)
                if zero_cnt<0:
                    return False
        return True


print(Solution().IsContinuous([0,3,2,6,4]))