import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        return list(heapq.merge(*matrix))[k-1]
        #有空的时候写下算法导论上的O(n)算法吧————分治，按5划分

print(Solution().kthSmallest([[1,2],[1,3]],2))




