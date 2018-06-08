# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        self.cnt = 0
        self.mergeSort(data, 0, len(data)-1)
        return self.cnt



    def mergeSort(self, data, start, end):
        if start >= end:
            return

        if start < end:
            mid = (start + end) // 2
            self.mergeSort(data, start, mid)
            self.mergeSort(data, mid+1, end)
            self.merge(data, start, mid, end)

    def merge(self, data, start, mid, end):
        aux = [0] * len(data)
        for i in range(start, end+1):
            aux[i] = data[i]
        i, j = start, mid+1
        k = start

        while (i<=mid and j<=end):
            if aux[i] <= aux[j]:
                data[k] = aux[i]
                k += 1
                i += 1
            else:
                data[k] = aux[j]
                k += 1
                j += 1
                self.cnt += mid - i + 1
                self.cnt %= 1000000007
        while (j <= end):
            data[k] = aux[j]
            k += 1
            j += 1
        while (i <= mid):
            data[k] = aux[i]
            k += 1
            i += 1


print(Solution().InversePairs([1,2,3,4,5,6,7,0]))

