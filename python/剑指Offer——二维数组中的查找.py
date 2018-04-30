# -*- coding:utf-8 -*-

# 不能用numpy真是天坑
# 哪天抽空看看numpy是怎么分片的，迭代器怎么写
# 代码写得像屎一样
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if (len(array) == 0 or len(array[0]) == 0):
            return False

        m = len(array) 
        n = len(array[0]) 

        midRow = m//2 
        midCol = n//2 

        if target == array[midRow][midCol]:
            return True

        if midRow == 0:
            return self.midSearch(target, array[0][:])
        elif midCol == 0:
            return self.midSearch(target, [array[i][0] for i in range(m)])

        elif target < array[midRow][midCol]:
            tag1 = self.Find(target, [array[i][:midCol] for i in range(midRow)])                       #array[:midRow,:midCol]  
            if tag1 == True:
                return True
            if self.midSearch(target, [array[i][midCol] for i in range(midRow)]) == True:              #array[:midRow,midCol]
                return True
            if self.midSearch(target, array[midRow][:midCol]) == True:
                return True
        else:                   
            tag1 = self.Find(target, [array[i][midRow+1:] for i in range(midCol+1,n)])                  #array[midRow+1:,midCol+1:]
            if tag1 == True:
                return True
            if self.midSearch(target,[array[i][midCol] for i in range(midRow+1,m)]) == True:            #array[midRow+1:,midCol]
                return True
            if self.midSearch(target,array[midRow][midCol+1:]) == True:                                
                return True

        tag2 = self.Find(target, [array[i][midCol+1:] for i in range(midRow)])                          #array[:midRow,midCol+1:]
        if tag2 == True:
            return True

        tag3 = self.Find(target, [array[i][:midCol] for i in range(midRow+1,m)])                         #array[midRow+1:,:midCol]

        return tag3

    def midSearch(self, target, array):
        left = 0
        right = len(array)-1

        while(left<=right):
            mid = (left+right)//2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return False


print(Solution().Find(3,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
