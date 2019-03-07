class Solution:
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        for a in A:
            a.reverse()
            for i in range(len(a)):
                a[i] = (a[i] + 1) % 2
        return A
