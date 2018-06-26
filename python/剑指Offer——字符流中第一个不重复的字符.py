# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.dic = {}
        self.s = ''
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dic[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char
        self.dic[char] = self.dic.get(char, 0) + 1