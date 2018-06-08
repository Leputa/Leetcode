# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        pos = self.getPositon(data, 0, len(data), k)
        if pos == -1:
            return 0
        cnt = 1
        pos1,pos2 = pos+1,pos-1
        while(pos1 < len(data) and data[pos1] == k):
            pos1 += 1
            cnt += 1
        while(pos2 >= 0 and data[pos2] == k):
            pos2 -= 1
            cnt += 1
        return cnt


    def getPositon(self, data, low, high, k):
        while(low < high):
            mid = (low + high) // 2
            if data[mid] == k:
                return mid
            elif data[mid] > k:
                high = mid
            else:
                low = mid + 1
        return -1


print(Solution().GetNumberOfK([1,2,3,3,3,3], 3))

