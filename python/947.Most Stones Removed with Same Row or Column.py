class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        pre = [i for i in range(len(stones) + 1)]
        rank = [1] * (len(stones) + 1)
        for i in range(1, len(stones)):
            for j in range(i+1, len(stones)+1):
                if stones[i-1][0] == stones[j-1][0] or stones[i-1][1] == stones[j-1][1]:
                    self.union(pre, rank, i, j)
        move = [0] * (len(stones) + 1)
        for i in range(1, len(pre)):
            move[self.find(pre, i)] += 1
        return max(move) - 1

    def union(self, pre, rank, x, y):
        fx = self.find(pre, x)
        fy = self.find(pre, y)
        if fx == fy:
            return 
        if rank[fx] < rank[fy]:
            pre[fx] = fy
            rank[fy] += rank[fx]
        else:
            pre[fy] = fx
            rank[fx] += rank[fy]

    def find(self, pre, x):
        if x == pre[x]:
            return x
        return self.find(pre, pre[x])