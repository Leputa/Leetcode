from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ret = []
        # 0 还未遍历； 1 正在遍历邻接点 3 已经结束
        # 如果当前结果是3， 直接返回true; 如果是2， 返回false（有环）
        flags = [0] * len(graph) 
        for i in range(len(graph)):
            if self.dfs(graph, i, flags):
                ret.append(i)
        return ret

    def dfs(self, graph, i, flags):
        if flags[i] == 2:
            return True
        if flags[i] == 1:
            return False   #loop
        flags[i] = 1
        for j in graph[i]:
            if flags[j] == 2:
                continue
            if flags[j] == 1 or self.dfs(graph, j, flags) == False:
                return False
        flags[i] = 2
        return True


if __name__ == '__main__':
    print(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
