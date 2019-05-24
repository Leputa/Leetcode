# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        inorder = []
        inorder_node = []
        tmpNode = root
        while(tmpNode != None or len(stack) != 0):
            while(tmpNode != None):
                stack.append(tmpNode)
                tmpNode = tmpNode.left
            if len(stack) != 0:
                tmpNode = stack.pop()
                inorder.append(tmpNode.val)
                inorder_node.append(tmpNode)
                tmpNode = tmpNode.right
        # 应该有效率更高的方法
        sort_inoder = sorted(inorder)
        exchange_index = []
        for idx, info in enumerate(zip(inorder, sort_inoder)):
            if info[0] != info[1]:
                exchange_index.append(idx)
        assert len(exchange_index) == 2
        inorder_node[exchange_index[0]].val = inorder[exchange_index[1]]
        inorder_node[exchange_index[1]].val = inorder[exchange_index[0]]
