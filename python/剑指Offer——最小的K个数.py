# -*- coding:utf-8 -*-
import heapq

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        ret = []
        if len(tinput) < k:
            return ret

        # write code here
        heapq.heapify(tinput)
        
        for i in range(k):
            ret.append(heapq.heappop(tinput))
        return ret

print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))

