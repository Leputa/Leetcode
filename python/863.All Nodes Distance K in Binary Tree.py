# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = dict()
        self.to_graph(None, root, graph)
        ret = set()
        self.dfs(graph, target, K, ret, None)
        return list(ret)

    def dfs(self, graph, target, K, ret, preNode):
        if K == 0:
            ret.add(target.val)
            return 
        for tmpNode in graph[target.val]:
            if tmpNode == preNode:
                continue
            self.dfs(graph, tmpNode, K-1, ret, target)

    def to_graph(self, preNode, tmpNode, graph):
        """
        type graph: dict
        """
        if graph.get(tmpNode.val) == None:
            graph[tmpNode.val] = []
        if preNode != None:
            graph[tmpNode.val].append(preNode)
        if tmpNode.left != None:
            graph[tmpNode.val].append(tmpNode.left)
            self.to_graph(tmpNode, tmpNode.left, graph)
        if tmpNode.right != None:
            graph[tmpNode.val].append(tmpNode.right)
            self.to_graph(tmpNode, tmpNode.right, graph) 

