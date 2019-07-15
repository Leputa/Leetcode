import heapq

class Solution:
    def kthSmallest_v2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        return list(heapq.merge(*matrix))[k-1]

    def kthSmallest_v1(self, matrix, k):
        left = matrix[0][0]
        right = matrix[len(matrix)-1][len(matrix[0])-1]
        while (left<right):
            mid = left + (right - left) / 2
            cnt = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] <= mid:
                        cnt += 1
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return left

    def kthSmallest(self, matrix, k):
        '''
        利用列递增的信息
        '''
        left = matrix[0][0]
        right = matrix[len(matrix)-1][len(matrix[0])-1]
        while (left < right):
            mid = left + (right - left) // 2
            cnt = self.search(matrix, mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return left

    def search(self, matrix, target):
        row, col = len(matrix)-1, 0
        cnt = 0
        while(row >= 0 and col < len(matrix)):
            if matrix[row][col] <= target:
                cnt += (row+1)
                col += 1
            else:
                row -= 1
        return cnt






print(Solution().kthSmallest_v1([[1,2],[1,3]],2))




