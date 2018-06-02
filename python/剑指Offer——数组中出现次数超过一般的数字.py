# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers == None or len(numbers) == 0:
            return ans

        ans = numbers[0]
        cnt = 1

        for i in range(1, len(numbers)):
            if numbers[i] == ans:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    ans = numbers[i]
                    cnt = 1
        
        if numbers.count(ans) > len(numbers)//2:
            return ans
        else:
            return 0



print(Solution().MoreThanHalfNum_Solution([2,2,2,2,2,1,3,4,5]))
# [1,2,3,2,2,2,5,4,2]