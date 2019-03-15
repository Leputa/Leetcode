class Solution:
    # 不使用路径压缩也不会超时
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = max([max(edge) for edge in edges])
        pre = [i for i in range(N+1)]
        rank = [1] * (N+1)
        for edge in edges:
            if self.is_union(edge[0], edge[1], pre, rank):
                return edge

    def is_union(self, x, y, pre, rank):
        fx = self.find_pre(x, pre)
        fy = self.find_pre(y, pre)
        if fx == fy:
            return True
        else:
            # 路径压缩
            if rank[fx] < rank[fy]:
                pre[fx] =  fy
                rank[fy] = rank[fx] + rank[fy]
            else:
                pre[fy] = fx
                rank[fx] = rank[fx] + rank[fy]
            return False

    def find_pre(self, x, pre):      
        if pre[x] == x:
            return x
        return self.find_pre(pre[x], pre)