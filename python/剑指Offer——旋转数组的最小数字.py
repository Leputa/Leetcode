# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0

        left,right = 0,len(rotateArray)-1

        if rotateArray[left]<rotateArray[right]:
            return rotateArray[left]
        
        while left < right:
            # print("left:" + str(left) + "  right:"+str(right))
            mid = (left + right)//2
            if rotateArray[mid] < rotateArray[0]:
                right = mid
            else:
                left = mid+1

        # print("left:" + str(left) + "  right:"+str(right))
        return min(rotateArray[left],rotateArray[right])


print(Solution().minNumberInRotateArray([2,1]))