# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd,even = -1,-1

        for i in range(len(array)):
            if array[i]%2 == 1:
                odd = i
            elif even == -1:
                even = i

            if even == -1 or odd == -1:
                continue

            if  odd > even:
                tmp = array[odd]
                for j in range(odd-1,even-1,-1):
                    array[j+1] = array[j]
                array[even] = tmp

                even += 1
                odd = -1

        return array


Solution().reOrderArray([1,2,3,4,5,6,7])

