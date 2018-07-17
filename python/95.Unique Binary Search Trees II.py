# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.genTree(1, n)

    def genTree(self, start, end):
        ret = []

        if start > end:
            ret.append(None)
            return ret
        if start == end:
            ret.append(TreeNode(start))
            return ret

        for i in range(start, end+1):
            leftList = self.genTree(start, i-1)
            rightList = self.genTree(i+1, end)

            for leftNode in leftList:
                for rightNode in rightList:
                    root = TreeNode(i)
                    root.left = leftNode
                    root.right = rightNode
                    ret.append(root)
        return ret









        