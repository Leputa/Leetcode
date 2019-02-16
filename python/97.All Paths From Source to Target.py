class Solution:
    def allPathsSourceTarget(self, graph: 'List[List[int]]') -> 'List[List[int]]':
        ret = []
        target = len(graph) - 1
        self.dfs(graph, 0, target, ret, [])
        return ret

    def dfs(self, graph, pos, target, ret, tmp_path):
        tmp_path.append(pos)
        if pos == target:
            ret.append(tmp_path[:])
        for next_node in graph[pos]:
            self.dfs(graph, next_node, target, ret, tmp_path)
            tmp_path.pop()
        