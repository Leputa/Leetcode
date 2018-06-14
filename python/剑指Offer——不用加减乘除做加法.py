# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2!=0 :                  # num2为0时，不存在进位
            tmp = num1 ^ num2
            num2 = (num1 & num2) << 1    # 添加进位
            num1 = tmp
        return tmp

print(Solution().Add(3, 5))
