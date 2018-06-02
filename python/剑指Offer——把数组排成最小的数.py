# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        
        if len(numbers) == 0:
            return ""

        strList = []
        length = 0
        for num in numbers:
            strList.append(str(num))
            if len(str(num)) > length:
                length = len(str(num))

        tupleList = []
        for s in strList:
            if len(s) < length:
                tupleList.append((s+(length-len(s))*s[-1], len(s)))
            else:
                tupleList.append((s, len(s)))
        tupleList.sort(key = lambda x: x[0])
        
        ret = ''
        for t in tupleList:
            ret += t[0][:t[1]]
        return int(ret)






print(Solution().PrintMinNumber([4, 3, 32, 321]))
