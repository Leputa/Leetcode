# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dic1 = {}  #char2index
        dic2 = {}  #char2cnt
        for i in range(len(s)):
            if dic1.get(s[i]) == None:
                dic1[s[i]] = i
            dic2[s[i]] = dic2.get(s[i], 0) + 1

        rnt = len(s)
        for k, v in dic2.items():
            if v == 1:
                index = dic1.get(k)
                if index < rnt:
                    rnt = index
        if rnt == len(s):
            return -1
        else:
            return rnt


