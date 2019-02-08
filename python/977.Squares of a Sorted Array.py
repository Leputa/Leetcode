class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        return sorted([item**2 for item in A])

print(Solution().sortedSquares([-4,-1,0,3,10]))