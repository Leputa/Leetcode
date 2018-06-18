# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        dic = {}
        for num in numbers:
            if dic.get(num, 0) == 0:
                dic[num] = 1
            else:
                duplication[0] = num
                return True
        return False
